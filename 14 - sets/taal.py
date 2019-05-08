def behoort_tot_taal(woord, taal):
    st = set(woord)
    st.discard(' ')
    return woord.issubset(taal) and len(st) > 0

def is_onleesbaar(woord,taal):
    st = set(woord)
    st.discard(' ')
    return st.indisjoint(taal)
