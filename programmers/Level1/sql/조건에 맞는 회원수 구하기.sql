select count(*) as users from user_info
 where age between 20 and 29
   and joined between '2021-01-01' and '2021-12-31';
