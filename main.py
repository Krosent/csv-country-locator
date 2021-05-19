import glob
import pandas
import pycountry


def update_locations():
    print("Program Started")
    so_users_df = pandas.concat(map(pandas.read_csv, glob.glob('data/*.csv')))
    print("Number of locations to update: \n", so_users_df.count())
    # take all rows from index 0 to index 499999
    for index, row in so_users_df.iloc[0:500000, :].iterrows():
        for c in pycountry.countries:
            if isinstance(row[5], str):
                if c.name in row[5]:
                    row[5] = c.name
                    so_users_df.at[index, 'Address']  = c.name
                    break
        print("Row at index: ", index, "has been updated!")
    print("finished, saving to file")
    so_users_df.to_csv("res.csv", index=False, header=True)
    print(so_users_df)


if __name__ == '__main__':
    # print_hi('PyCharm')
    update_locations()

