# Lab: Inconsistent security controls

Description : This lab's flawed logic allows arbitrary users to access administrative functionality that should only be available to company employees.

End goal : To solve the lab, access the admin panel and delete the user `carlos`.

## Analysis

- trying to access the admin panel directy -> unauthorized
- trying to add `@dontwannacry.com@MyEmail` -> invalid email
- tring to add `dedoxd2@dontwannacry.com.MyEmail` -> registered the email but didn't allow me access the admin panel
- finally updating the email to `dedoxd2@dontwannacry.com` -> didn't ask for anything and updated my email and allowed me to access the admin panel

## Metigation

- Send an OTP to the updated  email  to make sure that the user optain this email , and dont forget to protect it agains brute-forcing
