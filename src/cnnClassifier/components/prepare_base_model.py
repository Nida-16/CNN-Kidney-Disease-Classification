import tensorflow as tf
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig


class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    def get_base_model(self):
        config = self.config
        self.model = tf.keras.applications.vgg16.VGG16(
            include_top=config.params_include_top,
            weights=config.params_weights,
            input_shape=config.params_image_size
        )

        self.model.save(config.base_model_path)

    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation='softmax'
        )(flatten_in)

        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=['accuracy']
        )

        full_model.summary()
        return full_model

    def update_base_model(self):
        config = self.config
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=config.params_learning_rate
        )
        self.model.save(config.updated_model_path)
