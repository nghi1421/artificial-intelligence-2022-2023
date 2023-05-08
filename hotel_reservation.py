import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib

def predict_reservation(form_data):
      df = pd.read_csv('HotelReservations.csv')
      df = df.drop('Booking_ID', axis=1)

      label_encoder_type_of_meal_plan = LabelEncoder()
      label_encoder_room_type_reserved = LabelEncoder()
      label_encoder_market_segment_type = LabelEncoder()
      label_encoder_booking_status = LabelEncoder()


      df['type_of_meal_plan'] = label_encoder_type_of_meal_plan.fit_transform(df['type_of_meal_plan'])
      df['room_type_reserved'] = label_encoder_room_type_reserved.fit_transform(df['room_type_reserved'])
      df['market_segment_type'] = label_encoder_market_segment_type.fit_transform(df['market_segment_type'])
      df['booking_status'] = label_encoder_booking_status.fit_transform(df['booking_status'])


      type_of_meal_plan = dict(zip(label_encoder_type_of_meal_plan.classes_, label_encoder_type_of_meal_plan.transform(label_encoder_type_of_meal_plan.classes_)))
      room_type_reserved = dict(zip(label_encoder_room_type_reserved.classes_, label_encoder_room_type_reserved.transform(label_encoder_room_type_reserved.classes_)))
      market_segment_type = dict(zip(label_encoder_market_segment_type.classes_, label_encoder_market_segment_type.transform(label_encoder_market_segment_type.classes_)))
      booking_status = dict(zip(label_encoder_booking_status.classes_, label_encoder_booking_status.transform(label_encoder_booking_status.classes_)))

      print(type_of_meal_plan)
      print(room_type_reserved)
      print(market_segment_type)
      print(booking_status)

      filename = 'hotel_model.sav'
      loaded_model = joblib.load(filename)
      sample_test = {
            'no_of_adults': [int(form_data['no_of_adults'])],
            'no_of_children': [int(form_data['no_of_children'])],
            'no_of_weekend_nights': [int(form_data['no_of_weekend_nights'])],
            'no_of_week_nights': [int(form_data['no_of_week_nights'])],
            'type_of_meal_plan': [type_of_meal_plan[form_data['type_of_meal_plan']]],
            'required_car_parking_space': [form_data['required_car_parking_space']],
            'room_type_reserved': [room_type_reserved[form_data['room_type_reserved']]],
            'lead_time': [int(form_data['lead_time'])],
            'arrival_year': [int(form_data['arrival_year'])],
            'arrival_month': [int(form_data['arrival_month'])],
            'arrival_date': [int(form_data['arrival_date'])],
            'market_segment_type': [market_segment_type[form_data['market_segment_type']]],
            'repeated_guest': [form_data['repeated_guest']],
            'no_of_previous_cancellations': [int(form_data['no_of_previous_cancellations'])],
            'no_of_previous_bookings_not_canceled': [int(form_data['no_of_previous_bookings_not_canceled'])],
            'avg_price_per_room': [float(form_data['avg_price_per_room'])],
            'no_of_special_requests': [int(form_data['no_of_special_requests'])]
      };
      df = pd.DataFrame(sample_test)

      sample_pre_standard = df.values

      y_pred = loaded_model.predict(sample_pre_standard)

      return [key for key,value in booking_status.items() if value==y_pred]