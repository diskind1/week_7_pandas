from utils import *





def main():
    
    # Part 1: loading dataframe from json
    df = load_json()

    # Part 2
    df = replacing_existing_columns(df)

    df = removing_html_tags(df)
    df = replace_empty_value(df)
    df = creating_order_month(df)
    df = creating_a_high_value_order(df)
    df = creating_avg_rating_country(df)
    df = column_filtering(df)
    df = column_delivery_status(df)
    df = to_csv(df)


if __name__=="__main__":
    main()