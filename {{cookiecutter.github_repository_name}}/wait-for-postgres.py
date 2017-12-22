def pg_ready(host, port, dbuser='postgres', dbname='postgres',
             timeout=20, poll_freq=0.2):
    """Wait until a postgres instance is ready to receive connections.
    .. note::
        This requires psycopg2 to be installed.
    :type host: str
    :type port: int
    :type timeout: float
    :type poll_freq: float
    """
    import psycopg2
    t0 = time.time()
    while time.time() - t0 < timeout:
        try:
            conn = psycopg2.connect(
                "host={host} port={port} user={dbuser} "
                "dbname={dbname}".format(**vars())
            )
            logger.debug('Connected successfully.')
            conn.close()
            return True
        except psycopg2.OperationalError as ex:
            logger.debug("Connection failed: {0}".format(ex));
        time.sleep(poll_freq)

    logger.error('Postgres readiness check timed out.')
    return False
