import lib_dzne_filedata as _fd
import lib_dzne_math.na as _na
import lib_dzne_seq as _seq


def main(*, seq, sub_region_table, alignment_table):
    infos = [
        (sub_region_table, 'start', 'end'),
        (alignment_table, 'from', 'to'),
    ]
    previous_end = 0
    ans = _fd.TOMLData.load("")
    regions = list()
    for y in range(1, 4):
        for x in ('fr', 'cdr'):
            regions.append(f"{x}{y}")
    for reg in regions:
        for table, a, b in infos:
            if _na.isna(table):
                continue
            start = None
            end = None
            for index, (row,) in table.items():
                if index.startswith(reg):
                    start = row.get(a)
                    end = row.get(b)
                    break
            if _na.isna(start, end):
                continue
            ans[reg] = dict()
            if not (previous_end <= start - 1 <= end):
                raise ValueError()
            previous_end = end
            if _na.isna(seq):
                continue
            ans[reg] = _seq.data(
                seq=seq,
                go=start-1,
                end=end,
            )
            break
    return ans # in other version type is dict, but here it is of the type _fd.TOMLData



 
