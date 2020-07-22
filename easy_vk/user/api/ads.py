from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Ads(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def add_office_users(self, account_id: int = None, data: str = None) -> responses.AdsAddOfficeUsers:
        """
        Adds managers and/or supervisors to advertising account.
        
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe added managers. Description of 'user_specification' objects see below.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.addOfficeUsers'
        param_aliases = []
        response_type = responses.AdsAddOfficeUsers
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def check_link(self, account_id: int = None, link_type: str = None, link_url: str = None, campaign_id: int = None) -> responses.AdsCheckLink:
        """
        Allows to check the ad link.
        
        :param account_id: Advertising account ID.
        :param link_type: Object type: *'community' — community,, *'post' — community post,, *'application' — VK application,, *'video' — video,, *'site' — external site.
        :param link_url: Object URL.
        :param campaign_id: Campaign ID
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.checkLink'
        param_aliases = []
        response_type = responses.AdsCheckLink
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def create_ads(self, account_id: int = None, data: str = None) -> responses.AdsCreateAds:
        """
        Creates ads.
        
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe created ads. Description of 'ad_specification' objects see below.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.createAds'
        param_aliases = []
        response_type = responses.AdsCreateAds
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def create_campaigns(self, account_id: int = None, data: str = None) -> responses.AdsCreateCampaigns:
        """
        Creates advertising campaigns.
        
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe created campaigns. Description of 'campaign_specification' objects see below.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.createCampaigns'
        param_aliases = []
        response_type = responses.AdsCreateCampaigns
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def create_clients(self, account_id: int = None, data: str = None) -> responses.AdsCreateClients:
        """
        Creates clients of an advertising agency.
        
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe created campaigns. Description of 'client_specification' objects see below.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.createClients'
        param_aliases = []
        response_type = responses.AdsCreateClients
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def create_target_group(self, account_id: int = None, client_id: int = None, name: str = None, lifetime: int = None, target_pixel_id: int = None, target_pixel_rules: str = None) -> responses.AdsCreateTargetGroup:
        """
        Creates a group to re-target ads for users who visited advertiser's site (viewed information about the product, registered, etc.).
        
        :param account_id: Advertising account ID.
        :param client_id: 'Only for advertising agencies.', ID of the client with the advertising account where the group will be created.
        :param name: Name of the target group — a string up to 64 characters long.
        :param lifetime: 'For groups with auditory created with pixel code only.', , Number of days after that users will be automatically removed from the group.
        :param target_pixel_id: 
        :param target_pixel_rules: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.createTargetGroup'
        param_aliases = []
        response_type = responses.AdsCreateTargetGroup
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete_ads(self, account_id: int = None, ids: str = None) -> responses.AdsDeleteAds:
        """
        Archives ads.
        
        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with ad IDs.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.deleteAds'
        param_aliases = []
        response_type = responses.AdsDeleteAds
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete_campaigns(self, account_id: int = None, ids: str = None) -> responses.AdsDeleteCampaigns:
        """
        Archives advertising campaigns.
        
        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with IDs of deleted campaigns.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.deleteCampaigns'
        param_aliases = []
        response_type = responses.AdsDeleteCampaigns
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete_clients(self, account_id: int = None, ids: str = None) -> responses.AdsDeleteClients:
        """
        Archives clients of an advertising agency.
        
        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with IDs of deleted clients.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.deleteClients'
        param_aliases = []
        response_type = responses.AdsDeleteClients
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete_target_group(self, account_id: int = None, client_id: int = None, target_group_id: int = None) -> responses.BaseOk:
        """
        Deletes a retarget group.
        
        :param account_id: Advertising account ID.
        :param client_id: 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        :param target_group_id: Group ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.deleteTargetGroup'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_accounts(self) -> responses.AdsGetAccounts:
        """
        Returns a list of advertising accounts.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getAccounts'
        param_aliases = []
        response_type = responses.AdsGetAccounts
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_ads(self, account_id: int = None, ad_ids: str = None, campaign_ids: str = None, client_id: int = None, include_deleted: bool = None, only_deleted: bool = None, limit: int = None, offset: int = None) -> responses.AdsGetAds:
        """
        Returns number of ads.
        
        :param account_id: Advertising account ID.
        :param ad_ids: Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: 'Available and required for advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: Flag that specifies whether archived ads shall be shown: *0 — show only active ads,, *1 — show all ads.
        :param only_deleted: Flag that specifies whether to show only archived ads: *0 — show all ads,, *1 — show only archived ads. Available when include_deleted flag is *1
        :param limit: Limit of number of returned ads. Used only if ad_ids parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: Offset. Used in the same cases as 'limit' parameter.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getAds'
        param_aliases = []
        response_type = responses.AdsGetAds
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_ads_layout(self, account_id: int = None, ad_ids: str = None, campaign_ids: str = None, client_id: int = None, include_deleted: bool = None, limit: int = None, offset: int = None) -> responses.AdsGetAdsLayout:
        """
        Returns descriptions of ad layouts.
        
        :param account_id: Advertising account ID.
        :param ad_ids: Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: 'For advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: Flag that specifies whether archived ads shall be shown. *0 — show only active ads,, *1 — show all ads.
        :param limit: Limit of number of returned ads. Used only if 'ad_ids' parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: Offset. Used in the same cases as 'limit' parameter.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getAdsLayout'
        param_aliases = []
        response_type = responses.AdsGetAdsLayout
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_ads_targeting(self, account_id: int = None, ad_ids: str = None, campaign_ids: str = None, client_id: int = None, include_deleted: bool = None, limit: int = None, offset: int = None) -> responses.AdsGetAdsTargeting:
        """
        Returns ad targeting parameters.
        
        :param account_id: Advertising account ID.
        :param ad_ids: Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: 'For advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: flag that specifies whether archived ads shall be shown: *0 — show only active ads,, *1 — show all ads.
        :param limit: Limit of number of returned ads. Used only if 'ad_ids' parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: Offset needed to return a specific subset of results.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getAdsTargeting'
        param_aliases = []
        response_type = responses.AdsGetAdsTargeting
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_budget(self, account_id: int = None) -> responses.AdsGetBudget:
        """
        Returns current budget of the advertising account.
        
        :param account_id: Advertising account ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getBudget'
        param_aliases = []
        response_type = responses.AdsGetBudget
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_campaigns(self, account_id: int = None, client_id: int = None, include_deleted: bool = None, campaign_ids: str = None, fields: List[str] = None) -> responses.AdsGetCampaigns:
        """
        Returns a list of campaigns in an advertising account.
        
        :param account_id: Advertising account ID.
        :param client_id: 'For advertising agencies'. ID of the client advertising campaigns are retrieved from.
        :param include_deleted: Flag that specifies whether archived ads shall be shown. *0 — show only active campaigns,, *1 — show all campaigns.
        :param campaign_ids: Filter of advertising campaigns to show. Serialized JSON array with campaign IDs. Only campaigns that exist in 'campaign_ids' and belong to the specified advertising account will be shown. If the parameter is null, all campaigns will be shown.
        :param fields: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getCampaigns'
        param_aliases = []
        response_type = responses.AdsGetCampaigns
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_categories(self, lang: str = None) -> responses.AdsGetCategories:
        """
        Returns a list of possible ad categories.
        
        :param lang: Language. The full list of supported languages is [vk.com/dev/api_requests|here].
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getCategories'
        param_aliases = []
        response_type = responses.AdsGetCategories
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_clients(self, account_id: int = None) -> responses.AdsGetClients:
        """
        Returns a list of advertising agency's clients.
        
        :param account_id: Advertising account ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getClients'
        param_aliases = []
        response_type = responses.AdsGetClients
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_demographics(self, account_id: int = None, ids_type: str = None, ids: str = None, period: str = None, date_from: str = None, date_to: str = None) -> responses.AdsGetDemographics:
        """
        Returns demographics for ads or campaigns.
        
        :param account_id: Advertising account ID.
        :param ids_type: Type of requested objects listed in 'ids' parameter: *ad — ads,, *campaign — campaigns.
        :param ids: IDs requested ads or campaigns, separated with a comma, depending on the value set in 'ids_type'. Maximum 2000 objects.
        :param period: Data grouping by dates: *day — statistics by days,, *month — statistics by months,, *overall — overall statistics. 'date_from' and 'date_to' parameters set temporary limits.
        :param date_from: Date to show statistics from. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 — September 27, 2011, **0 — day it was created on,, *month: YYYY-MM, example: 2011-09 — September 2011, **0 — month it was created in,, *overall: 0.
        :param date_to: Date to show statistics to. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 — September 27, 2011, **0 — current day,, *month: YYYY-MM, example: 2011-09 — September 2011, **0 — current month,, *overall: 0.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getDemographics'
        param_aliases = []
        response_type = responses.AdsGetDemographics
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_flood_stats(self, account_id: int = None) -> responses.AdsGetFloodStats:
        """
        Returns information about current state of a counter — number of remaining runs of methods and time to the next counter nulling in seconds.
        
        :param account_id: Advertising account ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getFloodStats'
        param_aliases = []
        response_type = responses.AdsGetFloodStats
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_lookalike_requests(self, account_id: int = None, client_id: int = None, requests_ids: str = None, offset: int = None, limit: int = None, sort_by: str = None) -> responses.AdsGetLookalikeRequests:
        """
        :param account_id: 
        :param client_id: 
        :param requests_ids: 
        :param offset: 
        :param limit: 
        :param sort_by: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getLookalikeRequests'
        param_aliases = []
        response_type = responses.AdsGetLookalikeRequests
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_musicians(self, artist_name: str = None) -> responses.AdsGetMusicians:
        """
        :param artist_name: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getMusicians'
        param_aliases = []
        response_type = responses.AdsGetMusicians
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_office_users(self, account_id: int = None) -> responses.AdsGetOfficeUsers:
        """
        Returns a list of managers and supervisors of advertising account.
        
        :param account_id: Advertising account ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getOfficeUsers'
        param_aliases = []
        response_type = responses.AdsGetOfficeUsers
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_posts_reach(self, account_id: int = None, ids_type: str = None, ids: str = None) -> responses.AdsGetPostsReach:
        """
        Returns detailed statistics of promoted posts reach from campaigns and ads.
        
        :param account_id: Advertising account ID.
        :param ids_type: Type of requested objects listed in 'ids' parameter: *ad — ads,, *campaign — campaigns.
        :param ids: IDs requested ads or campaigns, separated with a comma, depending on the value set in 'ids_type'. Maximum 100 objects.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getPostsReach'
        param_aliases = []
        response_type = responses.AdsGetPostsReach
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_rejection_reason(self, account_id: int = None, ad_id: int = None) -> responses.AdsGetRejectionReason:
        """
        Returns a reason of ad rejection for pre-moderation.
        
        :param account_id: Advertising account ID.
        :param ad_id: Ad ID.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getRejectionReason'
        param_aliases = []
        response_type = responses.AdsGetRejectionReason
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_statistics(self, account_id: int = None, ids_type: str = None, ids: str = None, period: str = None, date_from: str = None, date_to: str = None, stats_fields: List[str] = None) -> responses.AdsGetStatistics:
        """
        Returns statistics of performance indicators for ads, campaigns, clients or the whole account.
        
        :param account_id: Advertising account ID.
        :param ids_type: Type of requested objects listed in 'ids' parameter: *ad — ads,, *campaign — campaigns,, *client — clients,, *office — account.
        :param ids: IDs requested ads, campaigns, clients or account, separated with a comma, depending on the value set in 'ids_type'. Maximum 2000 objects.
        :param period: Data grouping by dates: *day — statistics by days,, *month — statistics by months,, *overall — overall statistics. 'date_from' and 'date_to' parameters set temporary limits.
        :param date_from: Date to show statistics from. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 — September 27, 2011, **0 — day it was created on,, *month: YYYY-MM, example: 2011-09 — September 2011, **0 — month it was created in,, *overall: 0.
        :param date_to: Date to show statistics to. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 — September 27, 2011, **0 — current day,, *month: YYYY-MM, example: 2011-09 — September 2011, **0 — current month,, *overall: 0.
        :param stats_fields: Additional fields to add to statistics
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getStatistics'
        param_aliases = []
        response_type = responses.AdsGetStatistics
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_suggestions(self, section: str = None, ids: str = None, q: str = None, country: int = None, cities: str = None, lang: str = None) -> Union[responses.AdsGetSuggestions, responses.AdsGetSuggestionsRegions, responses.AdsGetSuggestionsCities, responses.AdsGetSuggestionsSchools]:
        """
        Returns a set of auto-suggestions for various targeting parameters.
        
        :param section: Section, suggestions are retrieved in. Available values: *countries — request of a list of countries. If q is not set or blank, a short list of countries is shown. Otherwise, a full list of countries is shown. *regions — requested list of regions. 'country' parameter is required. *cities — requested list of cities. 'country' parameter is required. *districts — requested list of districts. 'cities' parameter is required. *stations — requested list of subway stations. 'cities' parameter is required. *streets — requested list of streets. 'cities' parameter is required. *schools — requested list of educational organizations. 'cities' parameter is required. *interests — requested list of interests. *positions — requested list of positions (professions). *group_types — requested list of group types. *religions — requested list of religious commitments. *browsers — requested list of browsers and mobile devices.
        :param ids: Objects IDs separated by commas. If the parameter is passed, 'q, country, cities' should not be passed.
        :param q: Filter-line of the request (for countries, regions, cities, streets, schools, interests, positions).
        :param country: ID of the country objects are searched in.
        :param cities: IDs of cities where objects are searched in, separated with a comma.
        :param lang: Language of the returned string values. Supported languages: *ru — Russian,, *ua — Ukrainian,, *en — English.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getSuggestions'
        param_aliases = []
        if section in ['countries', 'positions', 'interest_categories', 'religions', 'user_devices', 'user_os', 'user_browsers']:
            response_type = responses.AdsGetSuggestions
        elif section == 'regions':
            response_type = responses.AdsGetSuggestionsRegions
        elif section == 'cities':
            response_type = responses.AdsGetSuggestionsCities
        else:
            response_type = responses.AdsGetSuggestionsSchools
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_target_groups(self, account_id: int = None, client_id: int = None, extended: bool = None) -> responses.AdsGetTargetGroups:
        """
        Returns a list of target groups.
        
        :param account_id: Advertising account ID.
        :param client_id: 'Only for advertising agencies.', ID of the client with the advertising account where the group will be created.
        :param extended: '1' — to return pixel code.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getTargetGroups'
        param_aliases = []
        response_type = responses.AdsGetTargetGroups
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_targeting_stats(self, account_id: int = None, client_id: int = None, criteria: str = None, ad_id: int = None, ad_format: int = None, ad_platform: str = None, ad_platform_no_wall: str = None, ad_platform_no_ad_network: str = None, link_url: str = None, link_domain: str = None, need_precise: bool = None) -> responses.AdsGetTargetingStats:
        """
        Returns the size of targeting audience, and also recommended values for CPC and CPM.
        
        :param account_id: Advertising account ID.
        :param client_id: 
        :param criteria: Serialized JSON object that describes targeting parameters. Description of 'criteria' object see below.
        :param ad_id: ID of an ad which targeting parameters shall be analyzed.
        :param ad_format: Ad format. Possible values: *'1' — image and text,, *'2' — big image,, *'3' — exclusive format,, *'4' — community, square image,, *'7' — special app format,, *'8' — special community format,, *'9' — post in community,, *'10' — app board.
        :param ad_platform: Platforms to use for ad showing. Possible values: (for 'ad_format' = '1'), *'0' — VK and partner sites,, *'1' — VK only. (for 'ad_format' = '9'), *'all' — all platforms,, *'desktop' — desktop version,, *'mobile' — mobile version and apps.
        :param ad_platform_no_wall: 
        :param ad_platform_no_ad_network: 
        :param link_url: URL for the advertised object.
        :param link_domain: Domain of the advertised object.
        :param need_precise: Additionally return recommended cpc and cpm to reach 5,10..95 percents of audience.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getTargetingStats'
        param_aliases = []
        response_type = responses.AdsGetTargetingStats
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_upload_url(self, ad_format: int = None, icon: int = None) -> responses.AdsGetUploadUrl:
        """
        Returns URL to upload an ad photo to.
        
        :param ad_format: Ad format: *1 — image and text,, *2 — big image,, *3 — exclusive format,, *4 — community, square image,, *7 — special app format.
        :param icon: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getUploadURL'
        param_aliases = []
        response_type = responses.AdsGetUploadUrl
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_video_upload_url(self) -> responses.AdsGetVideoUploadUrl:
        """
        Returns URL to upload an ad video to.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.getVideoUploadURL'
        param_aliases = []
        response_type = responses.AdsGetVideoUploadUrl
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def import_target_contacts(self, account_id: int = None, client_id: int = None, target_group_id: int = None, contacts: str = None) -> responses.AdsImportTargetContacts:
        """
        Imports a list of advertiser's contacts to count VK registered users against the target group.
        
        :param account_id: Advertising account ID.
        :param client_id: 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        :param target_group_id: Target group ID.
        :param contacts: List of phone numbers, emails or user IDs separated with a comma.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.importTargetContacts'
        param_aliases = []
        response_type = responses.AdsImportTargetContacts
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def remove_office_users(self, account_id: int = None, ids: str = None) -> responses.AdsRemoveOfficeUsers:
        """
        Removes managers and/or supervisors from advertising account.
        
        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with IDs of deleted managers.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.removeOfficeUsers'
        param_aliases = []
        response_type = responses.AdsRemoveOfficeUsers
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def update_ads(self, account_id: int = None, data: str = None) -> responses.AdsUpdateAds:
        """
        Edits ads.
        
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe changes in ads. Description of 'ad_edit_specification' objects see below.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.updateAds'
        param_aliases = []
        response_type = responses.AdsUpdateAds
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def update_campaigns(self, account_id: int = None, data: str = None) -> responses.AdsUpdateCampaigns:
        """
        Edits advertising campaigns.
        
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe changes in campaigns. Description of 'campaign_mod' objects see below.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.updateCampaigns'
        param_aliases = []
        response_type = responses.AdsUpdateCampaigns
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def update_clients(self, account_id: int = None, data: str = None) -> responses.AdsUpdateClients:
        """
        Edits clients of an advertising agency.
        
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe changes in clients. Description of 'client_mod' objects see below.
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.updateClients'
        param_aliases = []
        response_type = responses.AdsUpdateClients
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def update_target_group(self, account_id: int = None, client_id: int = None, target_group_id: int = None, name: str = None, domain: str = None, lifetime: int = None, target_pixel_id: int = None, target_pixel_rules: str = None) -> responses.BaseOk:
        """
        Edits a retarget group.
        
        :param account_id: Advertising account ID.
        :param client_id: 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        :param target_group_id: Group ID.
        :param name: New name of the target group — a string up to 64 characters long.
        :param domain: Domain of the site where user accounting code will be placed.
        :param lifetime: 'Only for the groups that get audience from sites with user accounting code.', Time in days when users added to a retarget group will be automatically excluded from it. '0' - automatic exclusion is off.
        :param target_pixel_id: 
        :param target_pixel_rules: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'ads.updateTargetGroup'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)
