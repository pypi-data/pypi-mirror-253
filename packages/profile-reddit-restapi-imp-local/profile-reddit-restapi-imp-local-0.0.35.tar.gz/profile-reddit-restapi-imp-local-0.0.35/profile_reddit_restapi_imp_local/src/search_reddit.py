import json
import sys
from .ProfileRedditConstants import (
    PROFILE_REDDIT_LOCAL_PYTHON_PACKAGE_COMPONENT_ID,
    PROFILE_REDDIT_LOCAL_PYTHON_PACKAGE_COMPONENT_NAME
)
import os
import tqdm
from logger_local.Logger import Logger
from logger_local.LoggerComponentEnum import LoggerComponentEnum
import praw
import requests
from group_remote.group_remote import GroupsRemote
from dotenv import load_dotenv
load_dotenv()


# TODO Use function from python-sdk to access environment vairables
REDDIT_CLIENT_ID = os.environ.get('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.environ.get('REDDIT_CLIENT_SECRET')
REDDIT_USERNAME = os.environ.get('REDDIT_USERNAME')

GROUP_PROFILE_RELATIONSHIP_TYPE_ID = 1

object_to_insert = {
    'component_id': PROFILE_REDDIT_LOCAL_PYTHON_PACKAGE_COMPONENT_ID,
    'component_name': PROFILE_REDDIT_LOCAL_PYTHON_PACKAGE_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'developer_email': 'yoav.e@circ.zone'
}

logger = Logger.create_logger(object=object_to_insert)


class Reddit:

    def __init__(self):
        logger.start()
        self.reddit = self._authenticate_reddit()
        logger.end()

    def _authenticate_reddit(self) -> praw.Reddit:

        logger.start()
        # TODO Let's add API-Management Indirect around it.
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=f"random_names (by u/{REDDIT_USERNAME})"
        )

        logger.end(object={'reddit': reddit})
        return reddit

    def get_subreddit_and_query(self, request: dict = None) -> dict:

        logger.start(object={'request': request})
        if request:
            subreddit_name, user_count = request['subreddit_name'], request['user_count']
            logger.end(object={'subreddit_name': subreddit_name, 'user_count': user_count})
            return subreddit_name, user_count

        subreddit_name = input("Enter subreddit name: ")

        num = input("Enter number of users to fetch (defult is no cap): ")

        user_count = int(num) if len(num) > 0 else None

        logger.end(object={'subreddit_name': subreddit_name, 'user_count': user_count})
        return subreddit_name, user_count

    def get_reddit_users_by_subreddit(self, subreddit, user_count: int):
        logger.start(object={'subreddit': subreddit.name, 'user_count': user_count})
        reddit_users_in_profile_json = []
        total = user_count

        total = float('inf') if total is None else total

        # TODO: when 'group' section is ready in ComprehensiveProfilesLocal, delete this line and
        #  add 'group' to reddit_users.append
        group_id = self._create_group_if_not_exists(subreddit.name)
        iteration = 0

        with tqdm.tqdm(total=total, desc="Getting users", file=sys.stdout) as pbar:
            for submission in subreddit.new(limit=None):
                if len(reddit_users_in_profile_json) >= total:
                    return reddit_users_in_profile_json
                for comment in submission.comments.list():
                    logger.info("Reddit user comment, iteration: " + str(iteration))
                    if len(reddit_users_in_profile_json) >= total:
                        return reddit_users_in_profile_json
                    if comment.author.name == 'AutoModerator':
                        continue
                    reddit_user_json = {
                        'profile': {
                            'name': str(comment.author.name),
                            'name_approved': False,
                            # TODO Please use Lang Code enum
                            'lang_code': "en",
                            # TODO Create and use enum VISIBILITY.CREATOR =1 from visibility-local-python-package 
                            'visibility_id': True,
                            'is_approved': False,
                            # TODO Please use profile enum
                            'profile_type_id': 1,
                            'stars': 0,
                            # TODO Let's create use DEFAULT_DIALOG_WORKFLOW_STATE_ID = 1 from dialog-workflow-local-python-package enum
                            'last_dialog_workflow_state_id': 1,
                            'comments': str(comment.author.comments),
                            'submissions': str(comment.author.submissions),
                            'created_utc': str(comment.author.created_utc),
                            'has_verified_email': str(comment.author.has_verified_email),
                            'is_employee': str(comment.author.is_employee),
                            'is_mod': str(comment.author.is_mod),
                            'is_gold': str(comment.author.is_gold),
                            'link_karma': str(comment.author.link_karma)
                        },

                        'storage': {
                            "url": str(comment.author.icon_img),
                            "filename": f'{comment.author.name}.jpg',
                                        "file_type": "Profile Image"
                        },

                        'reaction': {
                            'value': str(comment.author.comment_karma),
                            'image': None,
                            'title': 'comment karma',
                            'description': None
                        },
                        'group': {
                            'group_id': group_id,
                            'lang_code': "en",
                            'parent_group_id': None,
                            'is_interest': False,
                            'image': None,
                        },
                        'group_profile': {
                            'group_id': group_id,
                            'relationship_type_id': GROUP_PROFILE_RELATIONSHIP_TYPE_ID
                        }
                    }
                    reddit_users_in_profile_json.append(reddit_user_json)
                    logger.info("Reddit user data: " + str(reddit_user_json))
                    iteration += 1

                    # TODO Please update comment
                    pbar.update(1)
        logger.end(object={'reddit_users_in_profile_json': reddit_users_in_profile_json})
        return reddit_users_in_profile_json

    # TODO: when 'group' section is ready in ComprehensiveProfilesLocal, delete this private method
    # TODO Please don't delete this method until we see it is working
    def _create_group_if_not_exists(self, group_name: str):
        logger.start(object={'group_name': group_name})

        groups_remote_object = GroupsRemote()
        group = groups_remote_object.get_group_by_group_name(group_name)
        if group.status_code == requests.codes.no_content:
            group = groups_remote_object.create_group(group_name)
        group_content = json.loads(group.content.decode('utf-8'))
        group_id_str = group_content['data'][0]['id']
        group_id = int(group_id_str)

        logger.end(object={'group_id': group_id})
        return group_id
