import pandas as pd

# исходный csv-файл
file_path = 'D:\Test.csv - test.csv'
# базовый DF
src_df = pd.read_csv(file_path)


# Читаем весь DF
src_df
# Читаем первые несколько записей в DF
src_df.head()

# выбираем только нужные колонки и фильтруем
src_df[['order_id_new', 'metered_price', 'upfront_price']] \
    [(src_df['metered_price'] > round(src_df['upfront_price'] * 1.2,2)) \
     | \
     (src_df['metered_price'] < round(src_df['upfront_price'] * 0.8,2))] \
    #.head() 


# добавляем даты
artists_df['Stamp_datetime'] = pd.to_datetime(artists_df['Stamp'].str[:-10])
artists_df['Stamp_day'] = artists_df['Stamp_datetime'].dt.date # date
artists_df['Stamp_weekday'] = artists_df['Stamp_datetime'].dt.dayofweek # day of week, 0 – Monday, 6 – Sunday
artists_df['Stamp_hour'] = artists_df['Stamp_datetime'].dt.hour # hour

.to_excel('temp4.xlsx')
.to_csv('temp.csv')


df_4.groupby(['driver_device_uid_new', 'pred_quality'])['order_id_new'].count().to_excel('temp6.xlsx')  


from datetime import datetime

asd = '2020-02-02 0:01:16'
datetime_object = datetime.strptime(asd, '%Y-%m-%d %H:%M:%S')

#date('2020-02-02')
#'2020-02-02'.to_date()
print(datetime_object)
print(datetime_object.weekday())

df_2['date_col'] = pd.to_datetime(df_2['calc_created'])



general_message_data_df.rename(columns={"message_ts_datetime": "sms_cnt"}, inplace=True)
general_message_data_df['avg_month'] = general_message_data_df['sms_cnt'] / 30

.sort_values('message_ts_datetime', ascending = False)


print(src_df.shape[0], src_df.shape[1])

# Если есть вложенные агрегаты - надо использовать tuple
.sort_values(('user_id', 'count'), ascending = False)

.describe(include = 'all')

tmp_df = message_data_df \
    .groupby('user_id', as_index=False).agg({'message_ts': "count"})
tmp_df

df_left = pd.merge(signup_data_df, general_message_data_agg_df, how='left', on = 'user_id')

#df_5.plot.bar(rot=0)
    df_5.plot.bar()
    #df_5.plot()

# фильтрация по индексу (in)
consumption_data_df[consumption_data_df.index.isin((53, 55))]
# фильтрация по индексу (NOT in)
consumption_data_df[~consumption_data_df.index.isin((15042, 147934))]

# Выбор всех колонок в df + переименование итоговой суммы
df_2 = consumption_data_df.groupby(consumption_data_df.columns.tolist()).size().reset_index().\
    rename(columns={0:'records'})

# фильтрация по подстроке в строке
df[df['ids'].str.contains("ball")]

# Если надо проселектить колонку "на лету" без создания DF, то надо использовать Tuple
combined_cleaned_df.groupby(['SMP_Station'], as_index=False).agg({
    'artist-track': ['count', 'nunique']
})[[('SMP_Station',''), ('artist-track',   'count'), ('artist-track',   'nunique')]]

# Переименовать колонки
df_2.rename(columns={"ticket_id_new": "ticket_cnt", "overpaid_ride_ticket": "overpaid_ride_max"}, inplace=True)

# преобразование в str и обрезка строки
hour_created=src_df['calc_created'].str[11:-6]

# удаление колонок
tmp_df.drop(columns = ['Track', 'Artist'], inplace=True) 

# Замена null-значений
combined_df['SMP_Station'].fillna(combined_df['Feed_Name'], inplace = True)



#pandasql
import pandasql as ps
q = """
    select
        SMP_Station,
        count(*) as plays_cnt,
        count(distinct Artist_track) as songs_cnt,
        count(distinct Stamp_day) as days_played_cnt,
        min(Stamp_datetime) as min_date,
        max(Stamp_datetime) as max_date
    from 
        artist3_df 
    group by 
        SMP_Station
        
"""
radio1_df = ps.sqldf(q, locals())
print(ps.sqldf(q, locals()))

