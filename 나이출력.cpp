// 내 풀이1_나이는 태어나자마자 한 살로 치기 때문에 2022년 기준이라고 했지만 2023에서 age를 뺌
#include <string>
#include <vector>

using namespace std;

int solution(int age) {
    int answer = 2023-age;
    return answer;
}


// 내 풀이2
#include <string>
#include <vector>

using namespace std;

int solution(int age) {
    return 2023-age;
}


// 다른 사람의 풀이1_조건식.. 1 -> 2022 이런식
int solution(int age) {
    return  age == 1 ? 2022 : 
            age == 2 ? 2021 : 
            age == 3 ? 2020 :
            age == 4 ? 2019 :
            age == 5 ? 2018 :
            age == 6 ? 2017 :
            age == 7 ? 2016 :
            age == 8 ? 2015 :
            age == 9 ? 2014 :
            age == 10 ? 2013 :
            age == 11 ? 2012 :
            age == 12 ? 2011 :
            age == 13 ? 2010 :
            age == 14 ? 2009 :
            age == 15 ? 2008 :
            age == 16 ? 2007 :
            age == 17 ? 2006 :
            age == 18 ? 2005 :
            age == 19 ? 2004 :
            age == 20 ? 2003 :
            age == 21 ? 2002 :
            age == 22 ? 2001 :
            age == 23 ? 2000 :
            age == 24 ? 1999 :
            age == 25 ? 1998 :
            age == 26 ? 1997 :
            age == 27 ? 1996 :
            age == 28 ? 1995 :
            age == 29 ? 1994 :
            age == 30 ? 1993 :
            age == 31 ? 1992 :
            age == 32 ? 1991 :
            age == 33 ? 1990 :
            age == 34 ? 1989 :
            age == 35 ? 1988 :
            age == 36 ? 1987 :
            age == 37 ? 1986 :
            age == 38 ? 1985 :
            age == 39 ? 1984 :
            age == 40 ? 1983 :
            age == 41 ? 1982 :
            age == 42 ? 1981 :
            age == 43 ? 1980 :
            age == 44 ? 1979 :
            age == 45 ? 1978 :
            age == 46 ? 1977 :
            age == 47 ? 1976 :
            age == 48 ? 1975 :
            age == 49 ? 1974 :
            age == 50 ? 1973 :
            age == 51 ? 1972 :
            age == 52 ? 1971 :
            age == 53 ? 1970 :
            age == 54 ? 1969 :
            age == 55 ? 1968 :
            age == 56 ? 1967 :
            age == 57 ? 1966 :
            age == 58 ? 1965 :
            age == 59 ? 1964 :
            age == 60 ? 1963 :
            age == 61 ? 1962 :
            age == 62 ? 1961 :
            age == 63 ? 1960 :
            age == 64 ? 1959 :
            age == 65 ? 1958 :
            age == 66 ? 1957 :
            age == 67 ? 1956 :
            age == 68 ? 1955 :
            age == 69 ? 1954 :
            age == 70 ? 1953 :
            age == 71 ? 1952 :
            age == 72 ? 1951 :
            age == 73 ? 1950 :
            age == 74 ? 1949 :
            age == 75 ? 1948 :
            age == 76 ? 1947 :
            age == 77 ? 1946 :
            age == 78 ? 1945 :
            age == 79 ? 1944 :
            age == 80 ? 1943 :
            age == 81 ? 1942 :
            age == 82 ? 1941 :
            age == 83 ? 1940 :
            age == 84 ? 1939 :
            age == 85 ? 1938 :
            age == 86 ? 1937 :
            age == 87 ? 1936 :
            age == 88 ? 1935 :
            age == 89 ? 1934 :
            age == 90 ? 1933 :
            age == 91 ? 1932 :
            age == 92 ? 1931 :
            age == 93 ? 1930 :
            age == 94 ? 1929 :
            age == 95 ? 1928 :
            age == 96 ? 1927 :
            age == 97 ? 1926 :
            age == 98 ? 1925 :
            age == 99 ? 1924 :
            age == 100 ? 1923 :
            age == 101 ? 1922 :
            age == 102 ? 1921 :
            age == 103 ? 1920 :
            age == 104 ? 1919 :
            age == 105 ? 1918 :
            age == 106 ? 1917 :
            age == 107 ? 1916 :
            age == 108 ? 1915 :
            age == 109 ? 1914 :
            age == 110 ? 1913 :
            age == 111 ? 1912 :
            age == 112 ? 1911 :
            age == 113 ? 1910 :
            age == 114 ? 1909 :
            age == 115 ? 1908 :
            age == 116 ? 1907 :
            age == 117 ? 1906 :
            age == 118 ? 1905 :
            age == 119 ? 1904 :
            1903;
}


// 다른 사람의 풀이2
#include <time.h>
int solution(int age) {
    time_t t = time(NULL);
    struct tm* ptime = localtime(&t);
    return ptime->tm_year + ptime->tm_hour * 100 - ptime->tm_min % 2 - age;
}


// 다른 사람의 풀이3_'--age' 이 연산은 age 변수의 값을 먼저 1 감소시킨 후, 그 감소된 값을 2022에서 빼는 연산에 사용
#include <string>
#include <vector>
using namespace std;
int solution(int age) {
    return 2022 - --age;
}
