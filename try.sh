#!/bin/bash

url="http://serviziweb.tabaccai.it/voucherinps/VistaAdesioni.aspx"
method="POST"
__VIEWSTATE="/wEPDwUKMTgyMjc2ODU5Nw9kFgJmD2QWAgIDD2QWAgIBD2QWBgIJDw8WAh4EVGV4dAUKMTYvMDYvMjAxNmRkAgsPPCsADQEADxYEHgtfIUl0ZW1Db3VudGYeC18hRGF0YUJvdW5kZ2RkAg0PD2QPEBYDZgIBAgIWAxYCHg5QYXJhbWV0ZXJWYWx1ZQUCTk8WAh8DZRYCHwNlFgMCBWZmZGQYAgUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFJmN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkSW1hZ2VCdXR0b24xBSNjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJEdyaWRWaWV3MQ88KwAKAQhmZMwoFAyRXY3JYs9DkV3ejMlo7igN"
__EVENTVALIDATION="/wEWBALIz+SqCwLGn+kZAv6TqZYBAr28ifwM/IbG/fzNPry42IB1vrmIWYwKVkU="
cap_name='ctl00$ContentPlaceHolder1$tbCap'
cap_id="ctl00_ContentPlaceHolder1_tbCap"
comune_name='ctl00$ContentPlaceHolder1$tbComune'
comune_id="ctl00_ContentPlaceHolder1_tbComune"

cap_value="24022"
comune_value="Alzano Lombardo"

page=$(curl GET $url | grep -E "__VIEWSTATE|__EVENTVALIDATION" | cut -d" " -f5 | sed 's/^value="//' | sed 's/"$//')

echo page
echo $page
echo

echo page lines
while read -r line; do
    echo "$line"
		echo
done <<< "$page"


__VIEWSTATE=$(echo $page | cut -d" " -f1)
__EVENTVALIDATION=$(echo $page | cut -d" " -f2)

echo __VIEWSTATE
echo $__VIEWSTATE
echo
echo __EVENTVALIDATION
echo $__EVENTVALIDATION
echo

curl -X $method --form "$cap_name=$cap_value" --form "$comune_name=$comune_value" --form "__VIEWSTATE=$__VIEWSTATE" --form "__EVENTVALIDATION=$__EVENTVALIDATION" $url


