
import fabric.api

fabric.api.env.colorize_errors = True
fabric.api.env.settings = 'settings.development'

from tasks import *

lm = local.migration.MigrateAlias()
lt = local.test.TestAlias()
ls = local.server.ServerAlias()
lsh = local.shell.ShellAlias()
lgp = local.git.GitPullAlias()
lgph = local.git.GitPushAlias()
lgpp = local.git.GitPullPushAlias()
lpf = local.pip.PipFreezeAlias()
lpi = local.pip.PipInstallAlias()

sc = deployment.sass.SassCompileAlias()
bi = deployment.bower.BowerInstallAlias()
pi = deployment.pip.InstallRequirementsAlias()
gp = deployment.git.GitPullAlias()
cs = deployment.static.CollectStaticAlias()
up = deployment.process.UpstartRestart()
ng = deployment.nginx.NginxRestart()

D = deployment.DeploymentAlias()
d = deployment.ShortDeploymentAlias()

m = deployment.migration.MigrationAlias()

ln = local.notify.NotifyAlias()


staging = environment.Staging()
production = environment.Production()
