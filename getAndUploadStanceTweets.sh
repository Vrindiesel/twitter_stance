python3 searchTwitterCL_stance.py
# atheism
mv ./queries_for_amita/*theis* /home/nick/TwitterSearchToDatabase/queries_for_amita/atheism
mv ./queries_for_amita/*god* /home/nick/TwitterSearchToDatabase/queries_for_amita/atheism
mv ./queries_for_amita/*blasphemy* /home/nick/TwitterSearchToDatabase/queries_for_amita/atheism
mv ./queries_for_amita/*dogma* /home/nick/TwitterSearchToDatabase/queries_for_amita/atheism
mv ./queries_for_amita/*freethink* /home/nick/TwitterSearchToDatabase/queries_for_amita/atheism
mv ./queries_for_amita/*bible* /home/nick/TwitterSearchToDatabase/queries_for_amita/atheism
mv ./queries_for_amita/*islam* /home/nick/TwitterSearchToDatabase/queries_for_amita/atheism
mv ./queries_for_amita/*burninginhell* /home/nick/TwitterSearchToDatabase/queries_for_amita/atheism
mv ./queries_for_amita/*church* /home/nick/TwitterSearchToDatabase/queries_for_amita/atheism
mv ./queries_for_amita/*sacrilege* /home/nick/TwitterSearchToDatabase/queries_for_amita/atheism
mv ./queries_for_amita/*spiritual* /home/nick/TwitterSearchToDatabase/queries_for_amita/atheism
mv ./queries_for_amita/*jesus* /home/nick/TwitterSearchToDatabase/queries_for_amita/atheism
mv ./queries_for_amita/*praise* /home/nick/TwitterSearchToDatabase/queries_for_amita/atheism
mv ./queries_for_amita/*prayer* /home/nick/TwitterSearchToDatabase/queries_for_amita/atheism
mv ./queries_for_amita/*religi* /home/nick/TwitterSearchToDatabase/queries_for_amita/atheism
mv ./queries_for_amita/*awesome* /home/nick/TwitterSearchToDatabase/queries_for_amita/atheism
mv ./queries_for_amita/*agnostic* /home/nick/TwitterSearchToDatabase/queries_for_amita/atheism
# abortion
mv ./queries_for_amita/*abortion* /home/nick/TwitterSearchToDatabase/queries_for_amita/abortion
mv ./queries_for_amita/*unborn* /home/nick/TwitterSearchToDatabase/queries_for_amita/abortion
mv ./queries_for_amita/*standwithpp* /home/nick/TwitterSearchToDatabase/queries_for_amita/abortion
mv ./queries_for_amita/*defundpp* /home/nick/TwitterSearchToDatabase/queries_for_amita/abortion
mv ./queries_for_amita/*righttochoose* /home/nick/TwitterSearchToDatabase/queries_for_amita/abortion
mv ./queries_for_amita/*prolife* /home/nick/TwitterSearchToDatabase/queries_for_amita/abortion
mv ./queries_for_amita/*prochoice* /home/nick/TwitterSearchToDatabase/queries_for_amita/abortion
# climate
mv ./queries_for_amita/*climat* /home/nick/TwitterSearchToDatabase/queries_for_amita/climate_change
mv ./queries_for_amita/*globalwarming* /home/nick/TwitterSearchToDatabase/queries_for_amita/climate_change
mv ./queries_for_amita/*planet* /home/nick/TwitterSearchToDatabase/queries_for_amita/climate_change
mv ./queries_for_amita/*earth* /home/nick/TwitterSearchToDatabase/queries_for_amita/climate_change
mv ./queries_for_amita/*scam* /home/nick/TwitterSearchToDatabase/queries_for_amita/climate_change
mv ./queries_for_amita/*carbon* /home/nick/TwitterSearchToDatabase/queries_for_amita/climate_change
mv ./queries_for_amita/*deforestation* /home/nick/TwitterSearchToDatabase/queries_for_amita/climate_change
mv ./queries_for_amita/*fraud* /home/nick/TwitterSearchToDatabase/queries_for_amita/climate_change
mv ./queries_for_amita/*hoax* /home/nick/TwitterSearchToDatabase/queries_for_amita/climate_change
mv ./queries_for_amita/*risingsea* /home/nick/TwitterSearchToDatabase/queries_for_amita/climate_change
mv ./queries_for_amita/*lies* /home/nick/TwitterSearchToDatabase/queries_for_amita/climate_change
mv ./queries_for_amita/*keepitintheground* /home/nick/TwitterSearchToDatabase/queries_for_amita/climate_change
# hillary
mv ./queries_for_amita/*clinton* /home/nick/TwitterSearchToDatabase/queries_for_amita/hillary_clinton
mv ./queries_for_amita/*hillno* /home/nick/TwitterSearchToDatabase/queries_for_amita/hillary_clinton
mv ./queries_for_amita/*hillyes* /home/nick/TwitterSearchToDatabase/queries_for_amita/hillary_clinton
mv ./queries_for_amita/*hillary* /home/nick/TwitterSearchToDatabase/queries_for_amita/hillary_clinton
mv ./queries_for_amita/*withher* /home/nick/TwitterSearchToDatabase/queries_for_amita/hillary_clinton
mv ./queries_for_amita/*hilliar* /home/nick/TwitterSearchToDatabase/queries_for_amita/hillary_clinton
mv ./queries_for_amita/*benghazi* /home/nick/TwitterSearchToDatabase/queries_for_amita/hillary_clinton
# feminism
mv ./queries_for_amita/*femin* /home/nick/TwitterSearchToDatabase/queries_for_amita/feminism
mv ./queries_for_amita/*patriarchy* /home/nick/TwitterSearchToDatabase/queries_for_amita/feminism
mv ./queries_for_amita/*yesallwomen* /home/nick/TwitterSearchToDatabase/queries_for_amita/feminism
mv ./queries_for_amita/*womanpower* /home/nick/TwitterSearchToDatabase/queries_for_amita/feminism


python3 ./listJSONtoMySQL_stance.py iac_write 'IAC PASSWORD GOES HERE' localhost/iac

mv ./queries_for_amita/atheism/* /home/nick/TwitterSearchToDatabase/queries_for_amita/old
mv ./queries_for_amita/climate_change/* /home/nick/TwitterSearchToDatabase/queries_for_amita/old
mv ./queries_for_amita/hillary_clinton/* /home/nick/TwitterSearchToDatabase/queries_for_amita/old
mv ./queries_for_amita/feminism/* /home/nick/TwitterSearchToDatabase/queries_for_amita/old
mv ./queries_for_amita/abortion/* /home/nick/TwitterSearchToDatabase/queries_for_amita/old
