import sys
#print(sys.path)
sys.path.append('') ##get import to look in the working dir.

from shotglass2.shotglass import get_site_config
from shotglass2.takeabeltof.texting import TextMessage

import pdb


magic_numbers = {
    'valid_phone_number':{'number':'+15005550006','code':None},
    'non_mobile_number':{'number':'+15005550009','code':'12614'},
    'invalid_phone_number':{'number':'+15005550001','code':'121211'},
}


def update_config(text):
    # override with test credentials
    # Get the Twilio test config
    site_config = get_site_config()
    config = site_config['TWILIO_TESTING_CONFIGURATION']
    text._acct_sid = config['acct_sid']
    text._auth_token = config['auth_token']
    text._from_number = config['phone_number']
    
    
def test_successful_send():
    number_type = 'valid_phone_number'
    to_number = magic_numbers[number_type]['number']
    error_code = magic_numbers[number_type]['code'] # the code we expect
    # pdb.set_trace()
    text = TextMessage(to_number=to_number,message="This is a test")
    update_config(text)
        
    text.send()
    assert text.send_result
    assert text.send_result.error_code == error_code
    

def test_non_mobile_send():
    number_type = 'non_mobile_number'
    to_number = magic_numbers[number_type]['number']
    error_code = magic_numbers[number_type]['code'] # the code we expect
    text = TextMessage(to_number=to_number,message="This is a test")
    update_config(text)
        
    text.send()
    assert text.success == False
    assert 'is not a mobile number' in text.result_text
