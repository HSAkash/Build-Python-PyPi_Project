import tensorflow as tf
import os


class CropDiseaseML:
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        banana_model = tf.keras.models.load_model(os.path.join(self.BASE_DIR, 'banana.h5'))
        potato_model = tf.keras.models.load_model(os.path.join(self.BASE_DIR, 'potato.h5'))
        tomato_model = tf.keras.models.load_model(os.path.join(self.BASE_DIR, 'tomato.h5'))
        guava_model = tf.keras.models.load_model(os.path.join(self.BASE_DIR, 'guava.h5'))
        try:
            cauliflower_model = tf.keras.models.load_model(os.path.join(self.BASE_DIR, 'cauliflower.h5'))
        except:
            cauliflower_model = self.get_cauliflowerModel()
        self.model_dict = {
            'Banana':[banana_model, 224],
            'Guava':[guava_model, 224],
            'Cauliflower':[cauliflower_model , 224],
            'Potato':[potato_model, 224],
            'Tomato':[tomato_model, 112]   
        }
        
        self.class_name_dict = {
            'Banana':['Cordana leaf spot','Healthy','Pestalotiopsis palmarum','Sigatoka'],
            'Guava':['Canker','Dot leaf Disease', 'Healthy', 'Mummification','Rust'],
            'Cauliflower':['Bacterial spot rot','Black Rot','Downy Mildew', 'Healthy'],
            'Potato':['Early blight','Late blight','Healthy'],
            'Tomato':['Bacterial spot', 'Early blight', 'Late blight','Leaf Mold', 'Septoria leaf spot',
                'Spider mites Two spotted spider mite','Target Spot','Yellow Leaf Curl Virus','Mosaic virus','Healthy']
        }
    
    def get_cauliflowerModel(self):
        data_augmentation = tf.keras.Sequential([
            tf.keras.layers.experimental.preprocessing.RandomFlip("horizontal",input_shape=(224, 224, 3)),
            tf.keras.layers.experimental.preprocessing.RandomRotation(0.2),
            tf.keras.layers.experimental.preprocessing.RandomZoom(0.2),
            tf.keras.layers.experimental.preprocessing.RandomHeight(0.2),
            tf.keras.layers.experimental.preprocessing.RandomWidth(0.2)
        ], name ="data_augmentation")

        base_model = tf.keras.applications.EfficientNetB0(include_top=False)
        base_model.trainable= False

        #Setup model architecture with trainable top layers
        inputs = tf.keras.layers.Input(shape=(224,224,3), name='input_layer')
        x = data_augmentation(inputs)
        x = base_model(x, training=False)
        x = tf.keras.layers.GlobalAveragePooling2D(name='global_avg_pooling_layer')(x)
        outputs = tf.keras.layers.Dense(4, activation='softmax', name='output_layer')(x)
        best_weight_model = tf.keras.Model(inputs, outputs)



        best_weight_model.compile(
            loss='categorical_crossentropy',
            optimizer = tf.keras.optimizers.legacy.Adam(),
            metrics = ['accuracy']
        )
        best_weight_model.load_weights(os.path.join(self.BASE_DIR, "cauliflower_weights/cp.ckpt"))
        return best_weight_model


        
    def image_tf_reshape(self, image, img_shape):
        img = tf.image.resize(image, [img_shape, img_shape])
        img = tf.expand_dims(img, axis=0)
        return img
        
    def predict(self, image, category):
        """
        image type must be PIL or Numpy
        """
        
        try:
            model = self.model_dict[category][0]
            img_shape = self.model_dict[category][1]
            img = self.image_tf_reshape(image, img_shape)
            pred_prob = model.predict(img)
            arg_max_pred = pred_prob.argmax()
            return f"{category} {self.class_name_dict[category][arg_max_pred]}"
        except:
            pass
                
        return None
            

            
