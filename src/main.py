'''Run the pipeline as a program.'''

from pipeline import make_pipeline
import pipeline_base

if __name__ == '__main__':
    pipeline_base.main(make_pipeline)
