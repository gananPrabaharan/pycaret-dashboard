from utilities.general_utilities import check_bool


class Feature:
    def __init__(self, feature_id, feature_name, is_included=True, is_target=False):
        self.feature_id = feature_id
        self.feature_name = feature_name
        self.is_included = is_included
        self.is_target = is_target

    def to_dict(self):
        feature_dict = {
            "id": self.feature_id,
            "name": self.feature_name,
            "include": "Yes" if self.is_included else "No",
            "target": "Yes" if self.is_target else "No"
        }
        return feature_dict

    @staticmethod
    def from_dict(feature_dict):
        feature = Feature(
            feature_id=feature_dict["id"],
            feature_name=feature_dict["name"],
            is_included=check_bool(feature_dict["include"]),
            is_target=check_bool(feature_dict["target"])
        )

        return feature
