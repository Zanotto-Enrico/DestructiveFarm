CONFIG = {
    # Don't forget to remove the old database (flags.sqlite) before each competition.

    # The clients will run sploits on TEAMS and
    # fetch FLAG_FORMAT from sploits' stdout.
    'TEAMS': {'Team #{}'.format(i): '10.60.{}.1'.format(i)
              for i in range(0,43)},
    'FLAG_FORMAT': r'[A-Z0-9]{31}=',

    # This configures how and where to submit flags.
    # The protocol must be a module in protocols/ directory.

    #'SYSTEM_PROTOCOL': 'CCIT_http',
    #'SYSTEM_HOST': '10.10.0.1',
    #'SYSTEM_PORT': 31337,

    'SYSTEM_PROTOCOL': 'CCIT_http',
    'SYSTEM_URL': 'http://10.10.0.1:8080/flags',
    'SYSTEM_TOKEN': 'd7e873cfdcfd510662d3a086d64b4f3c',

    # 'SYSTEM_PROTOCOL': 'volgactf',
    # 'SYSTEM_HOST': '127.0.0.1',

    # 'SYSTEM_PROTOCOL': 'forcad_tcp',
    # 'SYSTEM_HOST': '127.0.0.1',
    # 'SYSTEM_PORT': 31337,
    # 'TEAM_TOKEN': 'your_secret_token',

    # The server will submit not more than SUBMIT_FLAG_LIMIT flags
    # every SUBMIT_PERIOD seconds. Flags received more than
    # FLAG_LIFETIME seconds ago will be skipped.
    'SUBMIT_FLAG_LIMIT': 300,
    'SUBMIT_PERIOD': 2,
    'FLAG_LIFETIME': 10 * 60,

    # Password for the web interface. You can use it with any login.
    # This value will be excluded from the config before sending it to farm clients.
    'SERVER_PASSWORD': 'bhackari',

    # Use authorization for API requests
    'ENABLE_API_AUTH': False,
    'API_TOKEN': 'd7e873cfdcfd510662d3a086d64b4f3c'
}
