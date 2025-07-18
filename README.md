#  نظام بنك الدم

##  وصف المشروع

نظام بنك الدم هو **منصة إلكترونية** تهدف إلى **تسهيل عمليات التبرع بالدم وإدارة طلبات الدم** بشكل رقمي وفعّال.

يتيح النظام للمستخدمين:

- حجز مواعيد التبرع بالدم عبر الإنترنت.
- ربط المتبرعين بالممرضين وتنظيم عمليات التبرع بطريقة منظمة.
- إدارة طلبات الدم ومطابقتها مع فصائل الدم المتوفرة.
- تمكين المدراء من مراقبة الأداء والعمليات بشكل كامل.

يعمل النظام من خلال واجهة سهلة الاستخدام وآمنة، ويدعم عدة أدوار مثل:

- المتبرع (Donor)
- المريض (Patient)
- الممرض (Nurse)
- المدير (Manager)

---

##  أعضاء الفريق

-  فرح خالد خدام
-  فرح عبد الناصر غلاونجي
-  الاء خالد عيروط
-  حسين عبدالله السيد احمد
-  علي مصطفى اغا

---

##  التقنيات المستخدمة

- **Django**: لبناء الواجهة الخلفية (API).

##  كيفية التشغيل
1. استنساخ المشروع
   - git clone https://github.com/alaaayrout/BloodBank.git
   -  cd BloodBank
2. إنشاء البيئة الافتراضية وتشغيل السيرفر
-  python -m venv virtual
- .\virtual\Scripts\activate
- pip install django
- pip install djangorestframework
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

---

## 📎 ملاحظات

هذا المشروع يهدف إلى تقديم حل رقمي فعّال وآمن لإدارة عمليات التبرع بالدم وربط المتبرعين بالمرضى والمراكز الطبية.
