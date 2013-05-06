"""
DBS Server default configuration file
"""
import os,logging,sys
from WMCore.Configuration import Configuration

ROOTDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 3)[0]
DBSVERSION = os.getenv('DBS3_VERSION')

sys.path.append(os.path.join(ROOTDIR,'auth/dbs'))

from DBSSecrets import dbs3_pl1_r
from DBSSecrets import dbs3_dg_i2
from DBSSecrets import dbs3_ig_i2

config = Configuration()
main = config.section_('main')
main.application = 'dbs'
main.port = 8250
main.index = 'data'

main.authz_defaults = { 'role':None, 'group' : None, 'site' : None}
security = main.section_('tools').section_("cms_auth")
security.key_file = os.path.join(ROOTDIR,'auth/wmcore-auth/header-auth-key')

app = config.section_('dbs')
app.admin = 'cms-service-webtools@cern.ch'
app.description = 'Data Bookkeeping Service 3'
app.title = 'CMS Data Bookkeeping Service'

views = config.section_('views')

data = views.section_('data')
data.object = 'dbs.web.DBSRestApi.DBSRestApi'
