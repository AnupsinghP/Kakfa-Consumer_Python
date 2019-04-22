import requests
from src.Settings import settings
class API:


    def sendData(self , messgae):
        """
        Upload readings to server
        :param messgae: Data for mongo db
        :return: success / failure
        """

        try:
            r = requests.put(settings['server'], data=messgae,
                         headers={
                             'Content-Type': 'application/json'
                         })
            if (r.status_code != 200):
                return False
            else:
                print('Data Sent')
                return True

        except requests.exceptions.RequestException as e:
            print("Reuquest Error: ",e)
            return False
        except ConnectionError as e:
            print("Connection Error",e)
            return False
        except:
            return False
