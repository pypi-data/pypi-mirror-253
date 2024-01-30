from location_local.location_local_constants import LocationLocalConstants
from data_source_local.src.data_source_enum import DataSource
from entity_type.entity_enum import EntityType
from .search_reddit import Reddit
from .ProfileRedditConstants import (
    PROFILE_REDDIT_LOCAL_PYTHON_PACKAGE_COMPONENT_ID,
    PROFILE_REDDIT_LOCAL_PYTHON_PACKAGE_COMPONENT_NAME
)
from logger_local.LoggerComponentEnum import LoggerComponentEnum
import json
from importer_local.ImportersLocal import ImportersLocal

from dotenv import load_dotenv
import sys
import os
sys.path.append(sys.path.append(os.getcwd()))
load_dotenv()
from logger_local.Logger import Logger  # noqa: E402
from user_context_remote.user_context import UserContext  # noqa: E402
from profiles_local.comprehensive_profile import ComprehensiveProfilesLocal  # noqa: E402

BRAND_NAME = os.environ.get('BRAND_NAME')
ENVIRONMENT_NAME = os.environ.get('ENVIRONMENT_NAME')

object_to_insert = {
    'component_id': PROFILE_REDDIT_LOCAL_PYTHON_PACKAGE_COMPONENT_ID,
    'component_name': PROFILE_REDDIT_LOCAL_PYTHON_PACKAGE_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'developer_email': 'yoav.e@circ.zone'
}

logger = Logger.create_logger(object=object_to_insert)

user_context = UserContext.login_using_user_identification_and_password()


if BRAND_NAME != 'Circlez':
    error = "please add BRAND_NAME to be Circlez to .env"
    logger.exception(error)
    raise Exception(error)

if ENVIRONMENT_NAME is None:
    error = "please add ENVIRONMENT_NAME to .env"
    logger.exception(error)
    raise Exception(error)


# TODO Is it relevant to inherit Comprehensive Profile Class?
class RedditImporter:
    def __init__(self):
        super().__init__()
        self.importer = ImportersLocal()
        self.user = UserContext()

    # We don't use this method anymore
    def process_reddit_user(reddit_user: dict) -> dict:
        logger.start(object={"reddit_user": reddit_user})

        comments = reddit_user['results']['profile']['comments']
        submissions = reddit_user['results']['profile']['submissions']

        comments_processed = []
        submissions_processed = []

        for comment in comments.new(limit=None):
            comments_processed.append(comment.body)

        for submission in submissions.new(limit=None):
            submissions_processed.append(submission.title)

        # profile-local expects name
        reddit_user['results']['profile']['name'] = reddit_user['results']['profile']['profile_name']
        reddit_user['results']['profile']['comments'] = comments_processed
        reddit_user['results']['profile']['submissions'] = submissions_processed

        logger.end(object={"reddit_user": reddit_user})
        return reddit_user

    # This method gets data of reddit users and saves it to the database
    # event is a json formatted as such:
    # {
    #     "subreddit_name": "subreddit_name",
    #     "user_count": "user_count"
    # }
    # It gets input from stdin if event is None, the input is the subreddit name(the group) and the number of users to save
    def handle(self, event: dict = None) -> None:
        """
        purpose:
            collect data on reddit users for a certain subreddit
        args:
            event: None for manual input(terminal),
            or a json formatted as such:
            {
                    "subreddit_name": "subreddit_name",
                    "user_count": "user_count"
            }

        example:
            main({"subreddit_name": "python", "user_count": 10})
            saves 10 users that commented on the python subreddit
            to the database

            main(None) asks for user input for subreddit name and user count
        """

        logger.start(object={"event": event})

        # collect the subreddit name and user count
        reddit = Reddit()
        subreddit_name, user_count = reddit.get_subreddit_and_query(event)
        subreddit = reddit.reddit.subreddit(subreddit_name)

        ##########################################################################
        # Here we need to add the subreddit to the groups table in the database,
        # so we can later add the users to the users table with the group name
        # as a foreign key
        ##########################################################################

        reddit_users_in_profile_json = reddit.get_reddit_users_by_subreddit(subreddit, user_count)
        inserted_ids = []

        # add a new group with the name of the subreddit, if DNE

        # try to fetch the group by name from the DB
        # if DNE, create a new group with the name of the subreddit
        # and send a event to insert it, else, do nothing

        # TODO What about connecting the profiles to groups? - Without importing the groups there is no big value.
        # group_id = get_group_by_name(subreddit_name) // pseudo code
        if reddit_users_in_profile_json:
            for reddit_user_in_profile_json in reddit_users_in_profile_json:

                # this step is inserting the user to the database
                # this needs to return the profile_id for us to be able to use the importer
                try:
                    profile_id = ComprehensiveProfilesLocal.insert(json.dumps(reddit_user_in_profile_json),
                                                                   user_context.get_effective_profile_preferred_lang_code())
                except Exception as e:
                    logger.error("an exception occurred while inserting profile " + str(reddit_user_in_profile_json)
                                 + " " + str(e))
                    continue

                if not profile_id:
                    logger.error("error inserting profile " + str(reddit_user_in_profile_json))
                    continue
                # insert to group profile the profile-id and the group-id
                # insert_to_group_profile(profile_id, group_id) // pseudo code

                # register in importer

                self.importer.insert(
                    data_source_id=DataSource.REDDIT_DATA_SOURCE_ID.value,
                    location_id=LocationLocalConstants.UNKNOWN_LOCATION_ID,
                    entity_type_id=EntityType.PERSONAL_PROFILE_ENTITY_TYPE_ID.value,
                    entity_id=profile_id,
                    url=f"https://www.reddit.com/r/{subreddit_name}",
                    user_id=self.user.get_effective_user_id()
                )
                inserted_ids.append(profile_id)

        else:
            logger.error("error no Reddit users found")

        logger.end(object={"inserted_ids": inserted_ids})
        return inserted_ids
