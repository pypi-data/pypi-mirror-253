class BuildInfo():
class BuildInfo():
    version = '1.1' # Version
    buildType = 'Release-PiPy' # Build type
    branding = 'SLoggy' # Branding
    brandingInLogs = f'[{branding}]' # Branding in logs
    gitHubLink = 'https://github.com/watermelon46/slogger' # Repository of project

from datetime import datetime

logfile = open('latest.log', 'w+')
logfile.truncate(0)

enable_printing = False
enable_branding = True

def change_branding(newbranding = None):
    """Change branding in logs from ''Sloggy'' to your."""
    BuildInfo.brandingInLogs = f'[{newbranding}]'

def enable_branding(mode = True):
    """Enable or disable branding in logs."""
    enable_branding = mode

def log(text):
    """Write anything in logs"""
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    if enable_branding == True:
        logtext = f'[{time}] {BuildInfo.brandingInLogs} {text}'
    else:
        logtext = f'[{time}] {text}'
    logfile.write(logtext + '\n')
    if enable_printing == True:
        print(logtext, end='')

def warn(text):
    """Write warn in logs"""
    log(f'[WARN] {text}')

def error(text):
    """Write error in logs"""
    log(f'[ERROR] {text}')

def info(text):
    """Write info in logs"""
    log(f'[INFO] {text}')

def user(text):
    """Write user input in logs"""
    log(f'[USER] {text}')

def custom(logtype, text):
    """Write custom log in logs"""
    log(f'[{logtype}] {text}')
    
def printing(mode = True):
    """Enable additional logs printing in terminal"""
    global enable_printing
    enable_printing = bool(mode)
    info(f'enable_printing changed to {mode}')

if BuildInfo.buildType != 'Release-PiPy':
    log(f'{BuildInfo.branding} {BuildInfo.version} {BuildInfo.buildType} started')
    info(f'Official GitHub repo of SLoggy - {BuildInfo.gitHubLink}')
