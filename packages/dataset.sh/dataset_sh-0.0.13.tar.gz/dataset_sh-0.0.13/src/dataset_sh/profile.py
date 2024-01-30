import os
import json
import warnings
from typing import List, Optional

from pydantic import BaseModel, Field, ValidationError
import dataset_sh.constants as DatasetConstants


class DatasetClientProfile(BaseModel):
    host: str
    key: str
    name: Optional[str] = None


class DatasetClientProfileConfig(BaseModel):
    profiles: List[DatasetClientProfile] = Field(default_factory=list)

    @staticmethod
    def load_profiles():
        config_file = DatasetConstants.CONFIG_JSON
        if os.path.exists(config_file):
            with open(config_file) as fd:
                try:
                    json_config = json.load(fd)
                    ret = DatasetClientProfileConfig(**json_config)
                    return ret
                except (ValidationError, json.decoder.JSONDecodeError):
                    warnings.warn('cannot parse profile config')
        return DatasetClientProfileConfig()

    def find_matching_profile(self, url, profile_name=None) -> Optional[DatasetClientProfile]:
        if profile_name is not None:
            for p in self.profiles:
                if p.name == profile_name:
                    return p
        else:
            for p in self.profiles:
                if url == p.host:
                    return p
        return None

    def save(self):
        config_file = DatasetConstants.CONFIG_JSON
        data = self.model_dump(mode='json')
        with open(config_file, 'w') as out:
            json.dump(data, out, indent=4)

    def add_profile(self, host, key, name='default'):
        for p in self.profiles:
            if p.name == name and p.host == host:
                p.key = key
                return self
        self.profiles.append(DatasetClientProfile(host=host, key=key, name=name))
        return self
