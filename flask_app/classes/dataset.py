from classes.feature import Feature


class Dataset:
    def __init__(self, data_df):
        self.data_df = data_df
        self.feature_list = self.extract_features_from_df()
        self.target_feature = self.get_target()
        self.train_df = None

    def extract_features_from_df(self):
        """
        Create list of features from data_df

        :return: list of Feature objects
        """

        feature_list = []
        for i, feature_name in enumerate(self.data_df.columns):
            feature = Feature(i, feature_name, True)
            feature_list.append(feature)

        return feature_list

    @staticmethod
    def validate_feature_dict_list(feature_dict_list):
        num_target = 0
        num_included = 0

        for feature_dict in feature_dict_list:
            if feature_dict["is_included"]:
                num_included += 1

            if feature_dict["is_target"]:
                num_target += 1
                if not feature_dict["is_included"]:
                    # Target feature must be included
                    raise ValueError

        # Required to have one target feature, and at least one other included feature
        if num_target != 1 or num_included == 1:
            return False

        return True

    def set_features(self, feature_dict_list):
        """
        Sets feature_list property from given feature_dict_list

        :param feature_dict_list: list of dictionaries containing feature information
        :return:
        """
        # Validate input feature dict list
        if not self.validate_feature_dict_list(feature_dict_list):
            raise ValueError

        feature_list = []
        for feature_dict in feature_dict_list:
            feature = Feature.from_dict(feature_dict)
            feature_list.append(feature)

        self.feature_list = feature_list
        self.target_feature = self.get_target()
        self.train_df = self.apply_filters()

    def get_target(self):
        """
        Returns feature that is_target if one exists

        :return: Feature object, or None
        """

        try:
            target = next((f for f in self.feature_list if f.is_target), None)
            return target
        except StopIteration:
            return None

    def apply_filters(self):
        """
        Creates DataFrame with user's feature configuration applied

        :return: DataFrame
        """
        columns_to_drop = [f.feature_name for f in self.feature_list if not f.is_included]
        train_df = self.data_df.drop(columns=columns_to_drop)
        return train_df

    def get_labels(self):
        """
        Extracts labels from target column of DataFrame

        :return: list of values from target columns
        """
        if self.target_feature is None:
            return None

        target_name = self.target_feature.feature_name
        labels = self.data_df[target_name].values
        return labels
