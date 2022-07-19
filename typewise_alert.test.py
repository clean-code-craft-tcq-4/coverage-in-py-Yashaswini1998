import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(70, 50, 100) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(100, 10, 80) == 'TOO_HIGH')

  def test_classify_temperature_breach(self):
    self.assertTrue(typewise_alert.classify_temperature_breach("PASSIVE_COOLING", -10) == 'TOO_LOW')
    self.assertTrue(typewise_alert.classify_temperature_breach("PASSIVE_COOLING", 20) == 'NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach("PASSIVE_COOLING", 50) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.classify_temperature_breach("HI_ACTIVE_COOLING", -20) == 'TOO_LOW')
    self.assertTrue(typewise_alert.classify_temperature_breach("HI_ACTIVE_COOLING", 25) == 'NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach("HI_ACTIVE_COOLING", 60) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.classify_temperature_breach("MED_ACTIVE_COOLING", -25) == 'TOO_LOW')
    self.assertTrue(typewise_alert.classify_temperature_breach("MED_ACTIVE_COOLING", 35) == 'NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach("MED_ACTIVE_COOLING", 55) == 'TOO_HIGH')


  def test_check_and_alert(self):
    breachType, message = typewise_alert.check_and_alert('TO_CONTROLLER', "PASSIVE_COOLING", 45)
    self.assertTrue(breachType == "TOO_HIGH")
    self.assertTrue(message == "0xfeed, TOO_HIGH")
    
    breachType, message = typewise_alert.check_and_alert('TO_EMAIL', "PASSIVE_COOLING", -5)    
    self.assertTrue(breachType == "TOO_LOW")
    self.assertTrue(message[0] == "To: a.b@c.com")
    self.assertTrue(message[1] == "Hi, the temperature is too low")


  def test_send_to_controller(self):
    self.assertTrue(typewise_alert.send_to_controller('TOO_LOW') == "0xfeed, TOO_LOW")

  def test_send_to_email(self):
    recepient_value, message = typewise_alert.send_to_email('TOO_LOW')
    self.assertTrue(recepient_value == "To: a.b@c.com")
    self.assertTrue(message == "Hi, the temperature is too low")

    recepient_value, message = typewise_alert.send_to_email('TOO_HIGH')
    self.assertTrue(recepient_value == "To: a.b@c.com")
    self.assertTrue(message == "Hi, the temperature is too high")
    
    

if __name__ == '__main__':
  unittest.main()
