from src.pipeline import Pipeline
from src.logger import Logger


def main():
    logger = Logger().get_logger()

    try:
        logger.info('starting pipeline')

        pipeline = Pipeline(logger=logger, csv_path='test\SegaGames.csv')
        pipeline.run()

        logger.info('finishing pipeline')
    except Exception as e:
        logger.error(f'An error ocurred: {e}')

main()
