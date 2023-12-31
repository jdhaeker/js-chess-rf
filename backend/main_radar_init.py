import time
from radar_v2 import RadarManager
from radar_utils.ioserver import IOServer
import random


sudo_password = 'radar123'
storage_directory = '/home/ci4r/PycharmProjects/ASL_game/data/'
cwd = '/home/ci4r/Desktop/77ghz/CLI/Release'
radar_path = '/home/ci4r/Desktop/77ghz/open_radar/open_radar_initiative-new_receive_test/' \
             'open_radar_initiative-new_receive_test/setup_radar/build'
model_file = '/home/ci4r/PycharmProjects/ASL_game/interactive-rf-main/backend/radar_utils/models/keras_model.h5'

duration = 3  # sec
filename = 'raw_game'
model_im_size = (224, 224)

socketServer = IOServer()
radar_mng = RadarManager(radar_path, cwd, sudo_password, storage_directory)
radar_mng.radar_init()
# radar_mng.record_and_plot(filename, duration=duration)
# pred = radar_mng.predict_sample(model_path=model_file, size=model_im_size)
# pred = None


def pred_to_server(pred):
    print('pred_to_server', pred)
    for i, p in enumerate(pred):
        confidence = round(p * 100 + 0, 2)
        socketServer.send('data', 'Class #' + str(i+1) + ' confidence: ' + str(confidence) + '%')


def generate_continuous_pred():
    # print('outer')
    eps = 0
    while True:
        # try:
        print('loop')
        # socketServer.send('data', 'Class #')
        radar_mng.record_and_plot(filename, duration=duration)
        pred = radar_mng.predict_sample(model_path=model_file, size=model_im_size)
        pred_to_server(pred)
        time.sleep(3)
        # except:
        #     print('RADAR ERROR!')
    #     socketServer.send('data', 'Class #' + str(1) + ' confidence: ' + str(2) + '%')
    # eps = random.randint(0, 10)
    # eps = 0
    # print(eps)
    #     pred_to_server(eps)
    # time.sleep(1)
generate_continuous_pred()

# socketServer.on("initialize", lambda x: generate_continuous_pred())
# socketServer.run()








