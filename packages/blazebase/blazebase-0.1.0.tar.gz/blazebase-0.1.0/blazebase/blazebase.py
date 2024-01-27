
import exceptions as exc
import firebase_admin as fb
import firebase_admin.auth as fba


def initialize_app(config):
    return BlazeBase(config)

class BlazeBase:
    
    def __init__(self, config):
                
        try:                                                                                                
            credentials = fb.credentials.Certificate(config.get("serviceAccount", None))
            self.app = fb.initialize_app(credential=credentials, options={
                "databaseURL": config.get("databaseURL", None),
                "storageBucket": config.get("storageBucket", None), 
                "projectId": config.get("projectId", None), 
                "databaseAuthVariableOverride": config.get("databaseAuthVariableOverride", None),
                "serviceAccountId": config.get("serviceAccountId", None),
                "httpTimeout": config.get("httpTimeout", None)
                })
        except Exception as e:
            raise exc.BlazeAuthenticationException(f"Could not authenticate the service account: {e}")

    
    def auth(self):
        return BlazeAuth(app=self.app)
    
    def database(self):
        return BlazeDatabase()
    
    def storage(self):
        return BlazeStorage()
        
class BlazeAuth:
    
    def __init__(self, app):
        self.app = app
    
    def verify_user_token(self, user_token):
        try:
            decoded_token = fba.verify_id_token(id_token=user_token, app=self.app, check_revoked=True)
            uid = decoded_token["uid"]
            return uid
        except Exception as e:
            raise exc.BlazeAuthenticationException(f"Could not verify token: {e}.")
        

class BlazeDatabase():
    pass


class BlazeStorage():
    pass
