import python_sdk_remote.utilities as utilities
import requests
from logger_local.Logger import Logger
from logger_local.LoggerComponentEnum import LoggerComponentEnum
from url_remote.action_name_enum import ActionName
from url_remote.component_name_enum import ComponentName
from url_remote.entity_name_enum import EntityName
from url_remote.url_circlez import OurUrl


GROUP_PROFILE_COMPONENT_ID = 211
GROUP_PROFILE_COMPONENT_NAME = "Group Profile Remote Python"
COMPONENT_CATEGORY = LoggerComponentEnum.ComponentCategory.Code.value
COMPONENT_TYPE = LoggerComponentEnum.ComponentType.Remote.value
DEVELOPER_EMAIL = "yarden.d@circ.zone"

obj = {
    'component_id': GROUP_PROFILE_COMPONENT_ID,
    'component_name': GROUP_PROFILE_COMPONENT_NAME,
    'component_category': COMPONENT_CATEGORY,
    'component_type': COMPONENT_TYPE,
    "developer_email": DEVELOPER_EMAIL
}

# TODO Please use array of GROUP_PROFILE_API_VERSION_ARRAY[EnvironmentName] to get the version per Environment
GROUP_PROFILE_API_VERSION = 1


class GroupProfilesRemote:

    def __init__(self):
        self.url_circlez = OurUrl()
        self.logger = Logger.create_logger(object=obj)
        self.brand_name = utilities.get_brand_name()
        self.env_name = utilities.get_environment_name()

    # TODO Can we move the is_test_data parameter to the constructor? 
    def create(self, group_id: str, relationship_type_id: str, is_test_data: bool = False):
        self.logger.start("Start create group-rofile-remote")
        effective_profile_id = str(
            self.logger.user_context.get_effective_profile_id())
        try:
            url = self.url_circlez.endpoint_url(
                brand_name=self.brand_name,
                environment_name=self.env_name,
                component_name=ComponentName.GROUP_PROFILE.value,
                entity_name=EntityName.GROUP_PROFILE.value,
                version=GROUP_PROFILE_API_VERSION,
                action_name=ActionName.CREATE_GROUP_PROFILE.value,  # "createGroupProfile",
            )
            self.logger.info(
                "Endpoint group profile - createGroupProfile action: " + url)

            group_profile_payload_json = {
                "groupId": f"{group_id}",
                "profileId": f"{effective_profile_id}",
                "relationshipTypeId": f"{relationship_type_id}",
                "is_test_data": f"{is_test_data}"
            }
            headers = utilities.create_authorization_http_headers(
                self.logger.user_context.get_user_jwt())
            response = requests.post(
                url=url, json=group_profile_payload_json, headers=headers)
            self.logger.end(
                f"End create group-profile-remote, response: {str(response)}")
            return response

        except requests.ConnectionError as e:
            self.logger.exception(
                "Network problem (e.g. failed to connect)", object=e)
        except requests.Timeout as e:
            self.logger.exception("Request timed out", e)
        except requests.RequestException as e:
            self.logger.exception(f"General error: {str(e)}", object=e)
        except Exception as e:
            self.logger.exception(
                f"An unexpected error occurred: {str(e)}", object=e)

        self.logger.end("End create group-profile-remote")

    # TODO Please make sure we have such with only group_id and profile_id without relationship_type_id

    def get_group_profiles_by_group_id_profile_id_relationship_type_id(self, group_id: int,
                                                                       profile_id: int,
                                                                       relationship_type_id: int):
        self.logger.start("Start get group-profile-remote")
        try:
            url = self.url_circlez.endpoint_url(
                brand_name=self.brand_name,
                environment_name=self.env_name,
                component_name=ComponentName.GROUP_PROFILE.value,
                entity_name=EntityName.GROUP_PROFILE.value,
                version=GROUP_PROFILE_API_VERSION,
                # "getGroupProfileByGroupIdProfileIdRelationshipTypeId",
                action_name=ActionName.GET_GROUP_PROFILE.value,
                query_parameters={
                    'groupId': group_id,
                    'profileId': str(self.logger.user_context.get_effective_profile_id()),
                    "relationshipTypeId": f"{relationship_type_id}"
                }
            )
            self.logger.info(
                "Endpoint group profile - getGroupProfileByGroupIdProfileId action: " + url)

            headers = utilities.create_authorization_http_headers(
                self.logger.user_context.get_user_jwt())
            response = requests.get(url, headers=headers)
            self.logger.end(
                f"End get group-profile-remote, response: {str(response)}")
            return response

        except requests.ConnectionError as error:
            self.logger.exception(
                "Network problem (e.g. failed to connect)", object=error)
            raise
        except requests.Timeout as error:
            self.logger.exception("Request timed out", object=error)
            raise
        except requests.RequestException as error:
            self.logger.exception(f"General error: {str(error)}", object=error)
            raise
        except Exception as error:
            self.logger.exception(
                f"An unexpected error occurred: {str(error)}", object=error)
            self.logger.end("End get group-profile-remote")
            raise

    def get_group_profiles_by_group_id_and_profile_id(self, group_id: int, profile_id: int):
        self.logger.start("Start get group-profile-remote")
        try:
            url = self.url_circlez.endpoint_url(
                brand_name=self.brand_name,
                environment_name=self.env_name,
                component_name=ComponentName.GROUP_PROFILE.value,
                entity_name=EntityName.GROUP_PROFILE.value,
                version=GROUP_PROFILE_API_VERSION,
                # "getGroupProfileByGroupIdProfileIdRelationshipTypeId",
                action_name=ActionName.GET_GROUP_PROFILE.value,
                query_parameters={
                    'groupId': group_id,
                    'profileId': str(self.logger.user_context.get_effective_profile_id())
                }
            )
            self.logger.info(
                "Endpoint group profile - getGroupProfileByGroupIdProfileId action: " + url)

            headers = utilities.create_authorization_http_headers(
                self.logger.user_context.get_user_jwt())
            response = requests.get(url, headers=headers)
            self.logger.end(
                f"End get group-profile-remote, response: {str(response)}")
            return response

        except requests.ConnectionError as error:
            self.logger.exception(
                "Network problem (e.g. failed to connect)", object=error)
            raise
        except requests.Timeout as error:
            self.logger.exception("Request timed out", object=error)
            raise
        except requests.RequestException as error:
            self.logger.exception(f"General error: {str(error)}", object=error)
            raise
        except Exception as error:
            self.logger.exception(
                f"An unexpected error occurred: {str(error)}", object=error)
            self.logger.end("End get group-profile-remote")
            raise

    def delete_group_profile(self, group_id: str, relationship_type_id: str):
        self.logger.start("Start delete group-profile-remote")
        try:
            url = self.url_circlez.endpoint_url(
                brand_name=self.brand_name,
                environment_name=self.env_name,
                component_name=ComponentName.GROUP_PROFILE.value,
                entity_name=EntityName.GROUP_PROFILE.value,
                version=GROUP_PROFILE_API_VERSION,
                action_name=ActionName.DELETE_GROUP_PROFILE.value,  # "deleteGroupProfile",
            )

            self.logger.info(
                "Endpoint group profile - deleteGroupProfile action: " + url)

            payload = {
                'groupId': group_id,
                'profileId': str(self.logger.user_context.get_effective_profile_id()),
                'relationshipTypeId': relationship_type_id
            }

            headers = utilities.create_authorization_http_headers(
                self.logger.user_context.get_user_jwt())

            response = requests.put(url, json=payload, headers=headers)
            self.logger.end(
                f"End delete group-profile-remote, response: {str(response)}")
            return response

        except requests.ConnectionError as e:
            self.logger.exception(
                "Network problem (e.g. failed to connect)", object=e)
            raise
        except requests.Timeout as e:
            self.logger.exception("Request timed out", object=e)
            raise
        except requests.RequestException as e:
            self.logger.exception(f"General error: {str(e)}", object=e)
            raise
        except Exception as e:
            self.logger.exception(
                f"An unexpected error occurred: {str(e)}", object=e)
            self.logger.end("End delete group-profile-remote")
            raise
