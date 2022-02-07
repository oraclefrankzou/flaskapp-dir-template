


from myapp import app
import logging


if __name__ == '__main__':
    logging.info('app start...')
    app.run(host=app.config['LISTENHOST'])