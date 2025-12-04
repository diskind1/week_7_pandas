import pandas as pd

def load_json():
    df = pd.read_json("orders_simple.json")
    return df
load_json


def replacing_existing_columns(df):
    df["total_amount"] = df["total_amount"].str.replace("$", "").astype(float)
    df["shipping_days"] = df["shipping_days"].astype(int)
    df["customer_age"] = df["customer_age"].astype(int)
    df["rating"] = df["rating"].astype(float)
    df["order_date"] = pd.to_datetime(df["order_date"])
    return df




def removing_html_tags(df):
    print(df.head(3))
    df["items_html"] = df["items_html"].str.replace("<b>|</b>|<br>|</br>", " ", regex=True)
    return df



def replace_empty_value(df):
    df["coupon_used"] = df["coupon_used"].str.replace('^\s*$', "no coupon", regex=True)
    return df

def creating_order_month(df):
    df["order_month"] = pd.to_datetime(df["order_date"]).dt.month
    return df

def creating_a_high_value_order(df):
    df["high_value_order"] = df["total_amount"] > df["total_amount"].mean()
    df.sort_values(by="total_amount", ascending=False, inplace=True)
    return df


def creating_avg_rating_country(df):
    df["avg_rating_country"] = df.groupby("country")["rating"].transform("mean")
    return df

def column_filtering(df):
    df = df.loc[(df["total_amount"] >1000) & (df["rating"] > 4.5)]
    return df

def column_delivery_status(df):
    df["delivery_status"] = "on time"
    df["delivery_status"][df["shipping_days"] > 7] = "delayed"
    return df


def to_csv(df):
    df.to_csv("clean_orders_[ID_NUMBER].csv")
    return df