# lar_projekts1

# Uzdevums

Projekta uzdevums ir izveidot lietotāja izvēlēta garuma paroles, kur pēc lietotāja izvēles var izvēlēties, vai iekļaut ciparus, lielos burtus, vai arī simbolus. Tā ģenerē 3 paroles, kuras tiek uzreiz ievietotas tīmekļa vietnē https://www.passwordmonster.com/, kur tiek pārbaudīts, cik droša ir šī parole. 

# Apraksts 

No sākuma lietotājam ir jāievada, kāds būs garums ģenerētajām parolēm. Tad tiek uzdoti jautājumi, vai iekļaut ciparus, lielos burtus, un simbolus. Uz tiem lietotājam ir jāatbild "yes", lai tie tiktu iekļauti. Programma izveido garu simbolu virkni, kura sastāv no izvēlētajiem simboliem. Pēc nejaušības, tiek izvēlēti simboli no tās, kuri tiek pievienoti parolei, līdz tā sasniedz izvēlēto garumu. Tālāk visas 3 paroles tiek ievietotas tīmekļa vietnē, kurā novērtē, cik droša tā ir, un parāda aptuveno laiku, kurā tā varētu tikt uzlauzta. Viss tiek izvadīts terminālī. 

# Izmantotās bibliotēkas

1. Selenium
Šī bibliotēka ļauj strādāt ar tīmekļa vietnēm, un tā ir svarīga, lai automatizētu darbības, šeit, ielīmē paroli un nokopē rezultātu. 
2. Time
Šī bibliotēka projektā tika izmantota lai aizkavētu laiku, un ļautu tīmekļa vietnei ielādēties. 
3. Random
Bibliotēka ļauj ģenerēt nejauši izvēlētus skaitļus. To izmantoju veidojot paroli, kad no visiem iespējamiem simboliem izvēlas nejaušu, kas tiek pievienots parolei. 

# Programmatūras izmantošanas metodes

1. Paroles izveidošana
Izveidotā parole ir nejauša, tāpēc lietotājs izvairās no iespējas, ka parole vairākās vietnēs ir vienāda, tāpēc ir drošāka

2. Paroles drošības pārbaude
Tāpēc, ka tiek izvadīts arī laiks, kurā varētu uzlauzt šo paroli, lietotājs tiek mudināts izvēlēties pēc iespējas drošāko. 