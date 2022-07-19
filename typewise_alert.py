
def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


def classify_temperature_breach(coolingType, temperatureInC):
  lowerLimit = 0
  upperLimit = 0
  if coolingType == 'PASSIVE_COOLING':
    lowerLimit = 0
    upperLimit = 35
  elif coolingType == 'HI_ACTIVE_COOLING':
    lowerLimit = 0
    upperLimit = 45
  else:
    lowerLimit = 0
    upperLimit = 40
  return infer_breach(temperatureInC, lowerLimit, upperLimit)


def check_and_alert(alertTarget, coolingType, temperatureInC):
  breachType =\
  classify_temperature_breach(coolingType, temperatureInC)
  if alertTarget == 'TO_CONTROLLER':
    message = send_to_controller(breachType)
  elif alertTarget == 'TO_EMAIL':
    message = send_to_email(breachType)
  return breachType, message


def send_to_controller(breachType):
  header = 0xfeed
  return (f'{hex(header)}, {breachType}')


def send_to_email(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    print(f'To: {recepient}')
    print('Hi, the temperature is too low')
    return(f'To: {recepient}', 'Hi, the temperature is too low')
  elif breachType == 'TOO_HIGH':
    print(f'To: {recepient}')
    print('Hi, the temperature is too high')
    return(f'To: {recepient}', 'Hi, the temperature is too high')
