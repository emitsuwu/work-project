import pandas as pd

def main():
    jackson = [[1,2,3,4], [11,12,13,14], [21,22,23,24], [31,32,33,34]]
    jackson_df = pd.DataFrame(jackson)
    print(jackson_df)
    jackson_df = jackson_df.transpose()
    new_list = []

    for x in range(jackson_df.shape[0]):
        new_list.append(jackson_df.loc[x, :].values.tolist())
    print(new_list)

    final_df = pd.DataFrame(new_list, columns=['a','b','c','d'])
    print(final_df)


    for x in range(final_df.shape[0]):
            print(f"{final_df['a'][x]}")
            print(f"{final_df['b'][x]}")
            print(f"{final_df['c'][x]}")
            print(f"{final_df['d'][x]}")



main()
