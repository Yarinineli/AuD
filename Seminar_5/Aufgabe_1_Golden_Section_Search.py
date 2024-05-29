import math as m

def f(x):
    return (x+(1/2))**2

def golden_section_search(l, r, f):
    # Die Formel für a', m'l und m'r
    a_strich = (2/(3+m.sqrt(5))) * (r - l)
    m_strich_l = l + a_strich
    m_strich_r = r - a_strich
    # Die y-Koordinate der Punkte m'l & m'r
    f(m_strich_l), f(m_strich_r)
    # Läuft so lange, bis der Abstand zwischen der linken Kante und der rechten Kante >= 0.001 ist. 
    while r - l >= 0.001:
        if f(m_strich_l) >= f(m_strich_r):
            l = m_strich_l
            m_strich_l = m_strich_r
            a_strich = (2/(3+m.sqrt(5))) * (r - l)
            m_strich_r = r - a_strich
            print(l, r)
        else:
            r = m_strich_r
            m_strich_r = m_strich_l
            a_strich = (2/(3+m.sqrt(5))) * (r - l)
            m_strich_l = l + a_strich
            print(l, r)
            
golden_section_search(-1000, 1000, f)