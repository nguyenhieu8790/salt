poolmng-config:
  file.recurse:
    - name: /opt/dl_app/conf/poolmng
    - user: tfx
    - group: tfx
    - file_mode: '0644'
    - dir_mode: '2755'
    - source: salt://dl_source/poolmng
    - template: jinja
    - context:
      dir_base: /opt/dl_app/
      log_dir: /opt/dl_app/logs/poolmng
      db_base: trsbase_dev
      db_rate: trsrate_dev
      db_account: haind
      db_password: haind
      db_host: 10.1.1.237
      dl_activemq: 10.1.10.175
      db_port: 3306

#poolmng_test:
#  file.managed:
#    - name: /opt/dl_app/conf/poolmng/doc2.conf
#    - source: salt://dl_source/poolmng/doc2.conf
#    - user: tfx
#    - group: tfx
#    - file_mode: '0644'
