topology-charts
===============

graph app with HighCharts



## Changes
- 2020/07/19
  - ����邩�A�\���l�����肵�����ʁA��������python�̕׋������˂�Django�����Ă݂�B
  - ���̃v���W�F�N�g�͎g���ĂȂ����S���̂Ă�B
  - ����邽�߂�docker�ŁB
  - docker offical�̎菇�ŐF�X�����Ȃ��B
    - https://docs.docker.jp/compose/django.html
  - �R�}���h�ƃG���[
    - docker-compose run web django-admin.py startproject composeexample .
    - composeexample/wsgi.py already exists, overlaying a project or app into an existing directory won't replace conflicting files
  - �F�X�������������t�@�C���������āA����炪�ז�����悤�������������������s�����肵���B
    - https://qiita.com/breakthrough/items/9929eefd11eefa255530
  - postgresql�N�����ɃG���[
    - Error: Database is uninitialized and superuser password is not specified.
    - ���b�Z�[�W�ʂ�docker-compose.yml�Ɋ��ϐ��ݒ�ǉ��B
  - �R�R�܂ŗ��ĉp��̂ق����ŐV���ł��Ă���悤�������̂ŎQ�Ɛ��ς���B
    - https://docs.docker.com/compose/django/


