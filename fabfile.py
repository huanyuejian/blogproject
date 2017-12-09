# python3
# coding:utf-8
"""fabric script"""
from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/huanyuejian/blogproject"
env.user = 'huanyue'
env.password = 'loveFCL95910.0'
env.hosts = ['huanyuejian.com']
env.port = '29636'

def deploy():
    source_folder = '/home/huanyue/sites/huanyuejian.com/blogproject'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-huanyuejian.com')
    sudo('service nginx reload')
