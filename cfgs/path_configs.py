import os
import glob

class PATH:
    
    def __init__(self):

        self.DATA_ROOT_PATH = './data_sample/'
        self.DATA_PATH = {
            'train': self.DATA_ROOT_PATH + 'train/train.csv',
            'test': self.DATA_ROOT_PATH + 'test/test.csv'
        }
        self.PRED_PATH = './results'
        self.CKPT_PATH = './ckpts'
        self.init_path()

    def check_path(self):
        """Check whether the dataset exists."""
        for mode in self.DATA_PATH:
            if not os.path.exists(self.DATA_PATH[mode]):
                print(self.DATA_PATH[mode] + ' IS NOT EXIST')
                exit(-1)

        print('Check path finished')
