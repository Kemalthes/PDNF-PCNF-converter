import pandas as pd


def main():
    try:
        print("Variables: 3 or 4 ?")
        varls = int(input())
        print("Enter result of boolean function with spaces")
        d3 = [0] * 7 + [1]
        d4 = [0] * 15 + [1]
        if varls == 3:
            print("1 2 3 4 5 6 7 8 <-tap enter")
            d3 = list(map(int, input().split()))
            if len(d3) != 2**varls or d3 == [0] * 2**varls or d3 == [1] * 2**varls:
                raise ValueError
        elif varls == 4:
            print("1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 <-tap enter")
            d4 = list(map(int, input().split()))
            if len(d4) != 2 ** varls or d4 == [0] * 2**varls or d4 == [1] * 2**varls:
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        print("No, bro")
        return

    df3 = pd.DataFrame([
        [0, 0, 0, d3[0]],
        [0, 0, 1, d3[1]],
        [0, 1, 0, d3[2]],
        [0, 1, 1, d3[3]],
        [1, 0, 0, d3[4]],
        [1, 0, 1, d3[5]],
        [1, 1, 0, d3[6]],
        [1, 1, 1, d3[7]]],
        columns=["x1", "x2", "x3", "F(x1,x2,x3)"])

    df4 = pd.DataFrame([
        [0, 0, 0, 0, d4[0]],
        [0, 0, 0, 1, d4[1]],
        [0, 0, 1, 0, d4[2]],
        [0, 0, 1, 1, d4[3]],
        [0, 1, 0, 0, d4[4]],
        [0, 1, 0, 1, d4[5]],
        [0, 1, 1, 0, d4[6]],
        [0, 1, 1, 1, d4[7]],
        [1, 0, 0, 0, d4[8]],
        [1, 0, 0, 1, d4[9]],
        [1, 0, 1, 0, d4[10]],
        [1, 0, 1, 1, d4[11]],
        [1, 1, 0, 0, d4[12]],
        [1, 1, 0, 1, d4[13]],
        [1, 1, 1, 0, d4[14]],
        [1, 1, 1, 1, d4[15]]],
        columns=["x1", "x2", "x3", "x4", "F(x1,x2,x3,x4)"])

    true3 = (~df3.loc[df3['F(x1,x2,x3)'] == 1, ['x1', 'x2', 'x3']].astype(bool)).astype('int8')
    true4 = (~df4.loc[df4['F(x1,x2,x3,x4)'] == 1, ['x1', 'x2', 'x3', 'x4']].astype(bool)).astype('int8')
    false3 = (df3.loc[df3['F(x1,x2,x3)'] == 0, ['x1', 'x2', 'x3']])
    false4 = (df4.loc[df4['F(x1,x2,x3,x4)'] == 0, ['x1', 'x2', 'x3', 'x4']])

    pdnf3 = (true3.apply(
        lambda trues: '({}{} * {}{} * {}{})'.format('!' * trues['x1'], 'x1', '!' * trues['x2'], 'x2', '!' * trues['x3'], 'x3'),
        axis=1).str.cat(sep=' v '))
    pdnf4 = (true4.apply(
        lambda trues: '({}{} * {}{} * {}{} * {}{})'.format('!' * trues['x1'], 'x1', '!' * trues['x2'], 'x2', '!' * trues['x3'], 'x3', '!' * trues['x4'], 'x4'),
        axis=1).str.cat(sep=' v '))
    pcnf3 = (false3.apply(
        lambda falses: '({}{} v {}{} v {}{})'.format('!' * falses['x1'], 'x1', '!' * falses['x2'], 'x2', '!' * falses['x3'], 'x3'),
        axis=1).str.cat(sep=' * '))
    pcnf4 = (false4.apply(
        lambda falses: '({}{} v {}{} v {}{} v {}{})'.format('!' * falses['x1'], 'x1', '!' * falses['x2'], 'x2', '!' * falses['x3'], 'x3', '!' * falses['x4'], 'x4'),
        axis=1).str.cat(sep=' * '))

    if varls == 3:
        print("PDNF / СДНФ:\n", pdnf3)
        print("PCNF / СКНФ:\n", pcnf3)
    elif varls == 4:
        print("PDNF / СДНФ:\n", pdnf4)
        print("PCNF / СКНФ:\n", pcnf4)


if __name__ == '__main__':
    main()
