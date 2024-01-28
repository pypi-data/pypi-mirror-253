from tensorflow.keras.callbacks import Callback
import time

class train_time(Callback):
    def on_train_begin(self, logs={}):
        self.times = []
        self.total_time = 0.0

    def on_epoch_begin(self, epoch, logs={}):
        self.epoch_start_time = time.time()

    def on_epoch_end(self, epoch, logs={}):
        epoch_time = time.time() - self.epoch_start_time
        self.times.append(epoch_time)
        self.total_time += epoch_time
        average_time_per_epoch = self.total_time / (epoch + 1)
        remaining_time = average_time_per_epoch * (self.params['epochs'] - epoch - 1)
        print("\nEpoch: {}/{}. Estimated time remaining: {:.2f} seconds.".format(
            epoch + 1, self.params['epochs'], remaining_time))


