import requests

url='https://operational-admin-test.tostar.top/manager-api/manager/activity/updateActivity'
data={
  "activityName": "Fastbull-默认新增邀新活动",
  "clientDispInfo":[
  {
    "langId": 2,
    "appEntranceDesc": "立即點擊開始賺取USD!",
    "name": "邀好友，賺USD！",
    "invitePrize": "邀好友註冊Trading Live, 邀請越多好友賺越多！獎勵次數無上限 ",
    "activityRuleSummary": "<p><span data-sheets-value=\"{&quot;1&quot;:2,&quot;2&quot;:&quot;邀好友註冊並登入 FastBull.live, 你和你好友皆可獲得最高 30 USD！邀請越多好友賺越多！(獎勵次數無上限)&quot;}\" data-sheets-userformat=\"{&quot;2&quot;:15233,&quot;3&quot;:{&quot;1&quot;:0},&quot;10&quot;:1,&quot;11&quot;:4,&quot;12&quot;:0,&quot;14&quot;:{&quot;1&quot;:2,&quot;2&quot;:0},&quot;15&quot;:&quot;宋体&quot;,&quot;16&quot;:11}\">邀好友註冊並登入Trading Live, 你和你好友皆可獲得最高 30 USD！邀請越多好友賺越多！(獎勵次數無上限)</span></p>",
    "activityRule": "<p>1. 活動獎勵：已註冊用戶擁有專屬的邀請連結，好友透過點擊你的專屬連結註冊後，你和你好友皆可獲得最高 30 USD，獎勵次數無上限，具體以活動頁面顯示為準。</p>\n<p>2. 有效邀請：透過專屬連結註冊並登入的真實用戶才算有效邀請。已註冊用戶每天可邀請的好友數不受限制，同一信箱/手機號碼註冊之用戶不可以被多個用戶邀請。同一IP和設備下登入的有效用戶有且只算首個帳號。在活動時間內邀請，且註冊成功並登入才算有效邀請。</p>\n<p>3. 獎勵提現：用戶於活動時間內達到提現門檻，可以在帳單頁面申請提現。</p>\n<p>4. 嚴禁之違規行為：<br />用戶不得從事任何違規異常或者不正當行為，一旦發現，Trading Live將有權取消其參與活動的資格。<br />1). 盜用身份，提供虛假資訊或者帳號；<br />2). 利用技術漏洞，規則漏洞，惡意獲取現金獎勵；<br />3). 同一IP和設備下多帳號參與活動；<br />4). 大量或非出於APP使用目的的註冊帳號；<br />5). 其他危害Trading Live形象或者社群規範的行為<br /><br /><br /></p>\n<p>活動最終解釋權歸Trading Live所有，如果有任何疑問請來信至service@trading.live</p>",
    "withdrawRule": "<p>1. 獎勵累計到提現門檻 50 USD 即可在帳單頁面申請提現。<br />2. 準確填寫數字錢包地址提交申請後，活動負責人員審核通過後將會發送贈金。<br />3. 已發送通知會透過系統訊息和信件的形式發送。請注意查收。<br />4. 任何問題請聯繫客服信箱:service@trading.live</p>",
    "userInvitedPrize": "註冊登入可得最高 30 USD ！立即開始無限邀好友，邀請越多賺越多！",
    "invitedPageAttention": "<p>1. 活動獎勵：透過好友邀請連結註冊並登入後，帳戶將可獲得系統隨機贈送的獎勵金，最高可達 30 USD。同時已註冊用戶擁有專屬邀請連結，好友通過你的專屬連結註冊後，，你和你好友皆可獲得系統贈送的隨機獎金，最高可達 30 USD，獎勵次數無上限!，a具體以活動頁面顯示為準。</p>\n<p>2. 獎勵提現：用戶於活動時間內達到提現門檻，可以在帳單頁面申請提現。</p>\n<p>3. 有效邀請：透過專屬連結註冊並登入的真實用戶才算有效邀請。已註冊用戶每天可邀請的好友數不受限制，但同一信箱/手機號碼註冊之用戶不可以被多個用戶邀請。同一IP和設備下登入的有效用戶有且只算首個帳號。在活動時間內邀請，且註冊成功並登入才算有效邀請。</p>\n<p>4. 嚴禁之違規行為：<br />用戶不得從事任何違規異常或者不正當行為，一旦發現，Trading Live 將有權取消其參與活動的資格。<br />1). 盜用身份，提供虛假資訊或者帳號；<br />2). 利用技術漏洞，規則漏洞，惡意獲取現金獎勵；<br />3). 同一IP和設備下多帳號參與活動；<br />4). 大量或非出於APP使用目的的註冊帳號；<br />5). 其他危害Trading Live形象或者社群規範的行為<br /><br />5. 本次活動僅限以下國家用戶參與：<br />沙特阿拉伯、卡塔爾、埃及、阿拉伯聯合酋長國、馬來西亞、新加坡、台灣和香港。</p>\n<p>活動最終解釋權歸Trading Live 所有，如果有任何疑問請來信至service@trading.live</p>",
    "title": "",
    "description": "",
    "keyword": ""
  },
  {
    "langId": 3,
    "appEntranceDesc": "Click to earn USD now!",
    "name": "Invite Friends \\n Get Unlimited Bonus",
    "invitePrize": "Invite your friends to sign up for Trading Live, and you'll both get up to 30 USD per invitee! Referral more, earn more!",
    "activityRuleSummary": "<p>Invite your friends to sign up for Trading Live, and you'll both get up to 30 USD per invitee! Referral more, earn more!</p>",
    "activityRule": "<p><strong>How does the TradingLive Referral Program work?</strong></p>\n<p>The TradingLive Referral Program rewards TradingLive users for inviting friends to sign up. Existing TradingLive users can copy a unique referral link, and share it with anyone who's not a current user or has not signed up with TradingLive before.&nbsp;</p>\n<p><strong>What You Both Get</strong></p>\n<p>If you are the referrer:&nbsp;You'll get up to USD 30 bonus for every qualified referral. A qualified referral means your referred friend who's not a current user or has not signed up with TradingLive before has signed up using your unique referral link.</p>\n<p>If you receive a referral link:&nbsp;You'll get up to USD 30 bonus once you've signed up with the unqiue referral link shared by your friend.&nbsp;</p>\n<p><strong>Withdrawal</strong></p>\n<p>You are eligible to be paid if your balance exceeds the withdrawal threshold. Please add your wallet address when submitting withdrawal application. Your withdrawal application will be reviewed. You will receive a notification and an email if your withdrawal application has been processed successfully.</p>\n<p><strong>TradingLive Referral Program Terms and Conditions </strong></p>\n<p>1. Your referred friend must sign up using a unique device (mobile, desktop or tablet) to prevent having their referral bonus forfeited;</p>\n<p>2. Some activities will disqualify you from earning referral bonuses, including:</p>\n<p>- Identity theft or fake account and info;</p>\n<p>- Get bonus using tech or rule loopholes;</p>\n<p>- Multiple accounts or device under the same IP address;</p>\n<p>- Create or maintain accounts with the intent of trying to get around TradingLive's rules;</p>\n<p>- Any similar activities considered by TradingLive in its sole discretion to be inconsistent with the TradingLive Referral Program;</p>\n<p>3. The TradingLive Referral Program is only applicable for users based in specific regions;</p>\n<p>4. All rights reserved by TradingLive. Please contact service@trading.live if you have any questions.</p>",
    "withdrawRule": "<p>1. Withdrawal can be initiated on the billing page if the rewards have accumulated to the withdrawal threshold of 50 USD.<br />2. Once the application has been submitted with an accurate wallet address, the event officer will initiate the withdrawal after approval.<br />3. Notification of the payment will be sent via system message and email. Please check the system message and email.<br />4. For any questions please contact: service@tradinglive</p>",
    "userInvitedPrize": "Sign up and get up to 30 USD per invitee!\\n\nUnlock your unlimited referral bonus from now!",
    "invitedPageAttention": "<p>1. Activity Reward: After registering and logging in, your account will receive a reward of up to 30 USD. Meanwhile, registered users have an exclusive invitation link, after your friends sign up through your exclusive link, both of you can get random reward money of up to 30 USD from the system per invitee. For the details please check the event page.<br />.</p>\n<p>2. Bonus withdrawal: Users who reach the withdrawal threshold during the event period can initiate a withdrawal on the billing page.</p>\n<p>3. Valid invitations: Only real users who have registered and logged in through the exclusive link are considered valid invitations. There is no limit to the number of invitations per day for registered users, and the same email/mobile phone number of registered users cannot be invited by multiple users. Valid users logged in under the same IP and device will only be counted as the first account. Invitations must take place during the event period and within the event area.</p>\n<p>4. Violations prohibited:<br />Users are not allowed to engage in any illegal, abnormal, or improper behavior, and Trading Live reserves all the right to disqualify them from participating in the event that they are found to be:<br />1). Providing false information or accounts<br />2). Using bugs and loopholes in the rules to get cash rewards.<br />3). Multiple accounts under the same IP and device to participate in the activity.<br />4). Registering accounts in bulk and not for the purpose of the APP use.<br />5). Any other actions that damageTrading Live's reputation or the community atmosphere.</p>\n<p>5. This event is only available for users in the following countries and regions:<br />Saudi Arabia, Qatar, Egypt, United Arab Emirates, Malaysia, Singapore, Taiwan, and Hong Kong.</p>\n<p>All rights reserved to Trading Live. For any questions, please contact us: service@trading.live</p>",
    "title": "",
    "description": "",
    "keyword": ""
  },
  {
    "langId": 4,
    "appEntranceDesc": "انقر لتحقق الأرباح الآن!",
    "name": "ادع الأصدقاء  واكسب USD",
    "invitePrize": "ادعوا أصدقائك للتسجيل في Trading Live\\n\nكلما دعوة أكثر، كلما ربحت أكثر!",
    "activityRuleSummary": "<p>ادعوا أصدقائك للتسجيل و الدخول إلى Trading Live، كلاكما يمكن أن يربح حتى 30 دولار أمريكي عن كلerer شخص يلبّي الدعوة! كلما دعوة أكثر، كلما ربحت أكثر!</p>",
    "activityRule": "<p>احتياطات<br />1. مكافأة الحدث: المستخدمون المسجلون لديهم رابط دعوة خاص. بعد تسجيل المدعو من خلال الرابط الخاص، يمكنك أنت والمدعو الحصول على مكافأة تصل إلى 30 USD عشوائيًا من المنصة في نفس الوقت. التفاصيل للعرض على صفحة الحدث.</p>\n<p>2. دعوة فعالة: سيتم اعتبار المستخدمين الحقيقيين المدعوين ناجحين فقط بعد تسجيل التطبيق تحت الرابط الخاص وتسجيل الدخول. لا يوجد حد لعدد الأشخاص المدعوين من قبل المستخدم كل يوم، ولا يمكن دعوة المستخدمين المسجلين بنفس عنوان البريد الإلكتروني / رقم الهاتف المحمول من قبل عدة مستخدمين. بالنسبة للمستخدمين الصالحين الذين يقومون بتسجيل الدخول باستخدام نفس عنوان IP والجهاز ، يتم التعرف فقط على الحساب الذي تم تسجيل الدخول إليه لأول مرة كحساب صالح. يتم تنفيذ النشاط فقط في المنطقة المحددة خلال وقت الحدث.</p>\n<p>3. سحب المكافأة: يمكن للمستخدمين الذين وصلوا إلى حد السحب خلال وقت النشاط بدء عملية سحب على صفحة الفاتورة.</p>\n<p>حظر الانتهاكات:<br />لا يُسمح للمستخدمين بالانخراط في أي سلوك غير قانوني أو غير طبيعي أو غير لائق ، بمجرد العثور عليه ، سيكون لـ Trading Live الحق في استبعادهم من المشاركة في النشاط.<br />1. سرقة الهوية وتقديم معلومات كاذبة أو رقم حساب<br />2. استخدام الثغرات الفنية وثغرات القواعد للحصول على مكافآت نقدية بشكل ضار.<br />3. المشاركة في الأنشطة مع حسابات متعددة تحت نفس عنوان IP والجهاز؛<br />4. سيتم إرسال إشعار الدفع عن طريق رسالة النظام والبريد الإلكتروني. يرجى الانتباه للتحقق؛<br />5. السلوكيات الأخرى التي تهدد سمعة Trading Live أو قواعد المجتمع.</p>\n<p>5. يقتصر هذا الحدث على المستخدمين من البلدان التالية:<br />المملكة العربية السعودية ، قطر ، مصر ، الإمارات العربية المتحدة ، ماليزيا ، سنغافورة ، تايوان ، هونغ كونغ.</p>\n<p>حق التفسير النهائي للحدث ينتمي إلى Trading Live ، إذا كان لديك أي أسئلة ، فيرجى إرسال بريد إلكتروني إلى service@trading.live</p>",
    "withdrawRule": "<p>1. إذا وصلت المكافأة المتراكمة إلى حد السحب البالغ 50 USD ، فيمكنك بدء السحب على صفحة الفاتورة.<br />2. بعد ملء عنوان المحفظة الرقمية بدقة وتقديم الطلب ، سيبدأ الشخص المسؤول عن الحدث الدفع بعد المراجعة.<br />3. سيتم إرسال إشعار الدفع عن طريق رسالة النظام والبريد الإلكتروني. يرجى الانتباه للتحقق.<br />4. إذا لديك أي أسئلة، يرجى الاتصال بـ service@trading.live</p>",
    "userInvitedPrize": "سجل وسجل الدخول لتحصل علي مكافأة  تصل إلى 30 USD! \\nابدأ في دعوة الأصدقاء بشكل غير محدود ، فكلما دعوت أكثر، زادت ربحك!",
    "invitedPageAttention": "<p>1. مكافأة الحدث: بعد التسجيل وتسجيل الدخول ، يمكن للحساب الحصول على مكافأة تصل إلى 30 USD عشوائيًا من المنصة . في نفس الوقت، المستخدمون المسجلون لديهم رابط دعوة خاص. بعد تسجيل المدعو من خلال الرابط الخاص، يمكنك أنت والمدعو الحصول على مكافأة تصل إلى 30 USD عشوائيًا من المنصة في نفس الوقت. التفاصيل للعرض على صفحة الحدث.</p>\n<p>2. سحب المكافأة: يمكن للمستخدمين الذين وصلوا إلى حد السحب خلال وقت النشاط بدء عملية سحب على صفحة الفاتورة.</p>\n<p>3. دعوة فعالة: سيتم اعتبار المستخدمين الحقيقيين المدعوين ناجحين فقط بعد تسجيل التطبيق تحت الرابط الخاص وتسجيل الدخول. لا يوجد حد لعدد الأشخاص المدعوين من قبل المستخدم كل يوم، ولا يمكن دعوة المستخدمين المسجلين بنفس عنوان البريد الإلكتروني / رقم الهاتف المحمول من قبل عدة مستخدمين. بالنسبة للمستخدمين الصالحين الذين يقومون بتسجيل الدخول باستخدام نفس عنوان IP والجهاز ، يتم التعرف فقط على الحساب الذي تم تسجيل الدخول إليه لأول مرة كحساب صالح. يتم تنفيذ النشاط فقط في المنطقة المحددة خلال وقت الحدث.</p>\n<p>حظر الانتهاكات:<br />لا يُسمح للمستخدمين بالانخراط في أي سلوك غير قانوني أو غير طبيعي أو غير لائق ، بمجرد العثور عليه ، سيكون لـ Trading Live الحق في استبعادهم من المشاركة في النشاط.<br />1. سرقة الهوية وتقديم معلومات كاذبة أو رقم حساب<br />2. استخدام الثغرات الفنية وثغرات القواعد للحصول على مكافآت نقدية بشكل ضار.<br />3. المشاركة في الأنشطة مع حسابات متعددة تحت نفس عنوان IP والجهاز؛<br />4. ليس لغرض الاستخدام ، قم بتسجيل الحسابات وإدارتها على دفعات على المنصة<br />5. السلوكيات الأخرى التي تهدد سمعة Trading Live أو قواعد المجتمع.</p>\n<p>5. هذا الحدث متاح للمستخدمين في هذه المناطق التالية فقط:</p>\n<p>المملكة العربية السعودية وقطر ومصر والإمارات العربية المتحدة وماليزيا وسنغافورة وتايوان وهونغ كونغ.</p>\n<p>حق التفسير النهائي للحدث ينتمي إلىTrading Live ، إذا كان لديك أي أسئلة ، فيرجى إرسال بريد إلكتروني إلى service@trading.live&nbsp;</p>",
    "title": "",
    "description": "",
    "keyword": ""
  },
  {
    "langId": 8,
    "appEntranceDesc": "马语-Klik untuk mula menjana pendapatan USD sekarang!",
    "name": "Jemput rakan dan dapatkan USD!",
    "invitePrize": "Jemput rakan-rakan untuk mendaftar untuk Trading Live, semakin banyak yang anda jemput, semakin banyak pendapatan anda!",
    "activityRuleSummary": "<p>Jemput rakan anda untuk mendaftar dan log masuk ke Trading Live, dan anda dan rakan anda boleh mendapatkan sehingga 30USD setiap orang pada masa yang sama! Semakin banyak anda menjemput, semakin banyak pendapatan anda!</p>",
    "activityRule": "<p>1. Ganjaran acara: Pengguna berdaftar mempunyai pautan jemputan eksklusif, dan selepas rakan mendaftar melalui pautan eksklusif anda, anda dan orang yang dijemput secara serentak boleh menerima ganjaran rawak sehingga 30USD setiap orang setiap orang, tertakluk kepada paparan pada halaman acara.</p>\n<p>2. Jemputan sah: Hanya pengguna sebenar yang mendaftar dan log masuk melalui pautan eksklusif dianggap sebagai jemputan yang sah. Tiada had untuk jemputan harian pengguna berdaftar, dan pengguna berdaftar dengan alamat e-mel / nombor telefon bimbit yang sama tidak boleh dijemput oleh berbilang pengguna. Pengguna yang sah log masuk di bawah alamat IP dan peranti yang sama telah dan hanya dikira sebagai akaun pertama. Jemputan mesti dilakukan pada masa acara, dalam kawasan acara.</p>\n<p>3. Pengeluaran ganjaran: Pengguna yang mencapai ambang pengeluaran semasa tempoh acara boleh memulakan pengeluaran pada halaman pengebilan.</p>\n<p>4. Larangan Pelanggaran:Pengguna tidak boleh terlibat dalam sebarang kelakuan yang tidak teratur, tidak normal atau tidak wajar dan Trading Live berhak untuk membatalkan kelayakan mereka daripada menyertai Promosi ini.</p>\n<p>1). Mencuri identiti, memberikan maklumat palsu atau nombor akaun</p>\n<p>2). Mengeksploitasi kelemahan teknikal dan kelemahan peraturan untuk mendapatkan ganjaran tunai dengan berniat jahat;</p>\n<p>3). Berbilang akaun di bawah IP dan peranti yang sama untuk mengambil bahagian dalam aktiviti;</p>\n<p>4). Penggunaan secara berkelompok atau bukan APP bagi akaun berdaftar, akaun penyelenggaraan;</p>\n<p>5) Tindakan lain yang membahayakan reputasi Trading Live atau Peraturan Komuniti5. Promosi ini hanya tersedia untuk pengguna dari negara dan wilayah berikut:Arab Saudi, Qatar, Mesir, UAE, Malaysia, Singapura, Taiwan, Hong Kong.Tafsiran akhir acara itu adalah milik Trading Live, jika anda mempunyai sebarang pertanyaan, sila e-mel service@trading.live</p>",
    "withdrawRule": "<p>1. Jika ganjaran telah terkumpul kepada ambang pengeluaran 50USD, anda boleh memulakan pengeluaran pada halaman pengebilan.</p>\n<p>2. Selepas mengisi alamat dompet digital dengan tepat dan mengemukakan permohonan, orang yang bertanggungjawab terhadap aktiviti tersebut akan memulakan pembayaran selepas semakan diluluskan.</p>\n<p>3. Pemberitahuan pembayaran berbayar akan dihantar melalui mesej sistem dan e-mel. Sila beri perhatian kepada cek</p>\n<p>4. Sila hubungi service@trading.live untuk sebarang pertanyaan</p>",
    "userInvitedPrize": "Daftar dan log sehingga 30USD setiap orang! Hidupkan jemputan rakan tanpa had, semakin banyak yang anda jemput, semakin banyak yang anda perolehi!",
    "invitedPageAttention": "<p>1. Ganjaran Acara: Selepas mendaftar dan log masuk melalui jemputan rakan, akaun akan dikreditkan ke sistem dengan ganjaran rawak sehingga 30USD. Pada masa yang sama, pengguna berdaftar mempunyai pautan jemputan eksklusif, selepas rakan mendaftar melalui pautan eksklusif anda, anda dan orang yang dijemput boleh mendapatkan ganjaran rawak sehingga 30USD setiap orang pada masa yang sama, tertakluk kepada paparan pada halaman acara.</p>\n<p>2. Pengeluaran ganjaran: Pengguna yang mencapai ambang pengeluaran semasa tempoh kempen boleh memulakan pengeluaran di halaman pengebilan.</p>\n<p>3. Jemputan sah: Hanya pengguna sebenar yang mendaftar dan log masuk melalui pautan eksklusif dianggap sebagai jemputan yang sah. Tiada had untuk jemputan harian pengguna berdaftar, dan pengguna berdaftar dengan alamat e-mel / nombor telefon bimbit yang sama tidak boleh dijemput oleh berbilang pengguna. Pengguna sah log masuk di bawah alamat IP dan peranti yang sama mempunyai dan hanya dikira sebagai akaun pertama. Jemputan mesti dilakukan pada masa acara, dalam kawasan acara.</p>\n<p>4. Larangan Pelanggaran:Pengguna tidak boleh terlibat dalam sebarang kelakuan yang tidak teratur, luar biasa atau tidak wajar dan Trading Live berhak untuk membatalkan kelayakan mereka daripada menyertai Promosi ini.</p>\n<p>1) Mencuri identiti, memberikan maklumat palsu atau nombor akaun;</p>\n<p>2). Mengeksploitasi kelemahan teknikal dan kelemahan peraturan untuk mendapatkan ganjaran tunai dengan berniat jahat;</p>\n<p>3). Berbilang akaun di bawah IP dan peranti yang sama untuk mengambil bahagian dalam aktiviti;</p>\n<p>4). Penggunaan secara berkelompok atau bukan APP bagi akaun berdaftar, akaun penyelenggaraan;</p>\n<p>5) Tindakan lain yang membahayakan reputasi Trading Live atau Peraturan Komuniti.</p>\n<p>5. Promosi ini hanya tersedia untuk pengguna di negara-negara berikut:Arab Saudi, Qatar, Mesir, UAE, Malaysia, Singapura, Taiwan, Hong Kong.Tafsiran akhir acara itu adalah milik Trading Live, jika anda mempunyai sebarang pertanyaan, sila e-mel service@trading.live</p>",
    "title": "null",
    "description": "null",
    "keyword": "null"
  },
  {
    "langId": 9,
    "appEntranceDesc": "คลิกที่นี่เพื่อเริ่มรับดอลล่าร์ทันที!",
    "name": "เชิญเพื่อน รับดอลล่าร์",
    "invitePrize": "เชิญเพื่อนของคุณลงทะเบียนบัญชี Trading Live\\n\nแนะนำมากขึ้น รับมากขึ้น!",
    "activityRuleSummary": "<p>เชิญเพื่อนของคุณลงทะเบียนและเข้าสู่ระบบบัญชี Trading Liveเมื่อเพื่อนของคุณเข้าสู่ระบบสำเร็จ คุณจะสามารถรับเงินสูงสุด30ดอลล่าร์/ต่อคน! แนะนำมากขึ้น รับมากขึ้น!</p>",
    "activityRule": "<p>1.รางวัลกิจกรรม: ผู้ใช้ที่ลงทะเบียนจะมีลิงก์คำเชิญพิเศษ หลังจากเพื่อนลงทะเบียนผ่านลิงก์พิเศษของคุณ คุณและผู้ได้รับเชิญสามารถได้รับเงินสูงสุด30ดอลล่าร์/ต่อคนจากระบบ ข้อมูลรายละเอียดจะขึ้นอยู่กับการแสดงบนหน้ากิจกรรม!</p>\n<p>2.คำเชิญที่ถูกต้อง: ผู้ใช้จริงที่ลงทะเบียนและเข้าสู่ระบบภายใต้ลิงก์พิเศษเป็นคำเชิญที่ถูกต้อง ผู้ใช้ลงทะเบียนจะได้รับคำเชิญไม่จำกัดทุกวัน แต่ผู้ใช้ลงทะเบียนซึ่งมีอีเมล/หมายเลขโทรศัพท์เดียวกันไม่สามารถเชิญจากผู้ใช้หลายคน ผู้ใช้จริงต้องเข้าสู่ระบบภายใต้ IP และอุปกรณ์เดียวกันจะเป็นบัญชีแรกเท่านั้น คำเชิญจะต้องเกิดขึ้นในเวลากิจกรรมและภายในพื้นที่กิจกรรม!</p>\n<p>3.การถอนรางวัล: ผู้ใช้ที่ถึงเกณฑ์การถอนเงินภายในเวลากิจกรรมสามารถเริ่มการถอนได้ในหน้าบิล</p>\n<p>4.ห้ามของกิจกรรมการละเมิด:&nbsp;<br />ผู้ใช้ไม่สามารถมีกิจกรรมที่ผิดกฏหมาย การละเมิด ผิดปกติหรือไม่เหมาะสม เมื่อเราพบ FastBull.live จะมีสิทธิ์ตัดสิทธิ์จากการเข้าร่วมกิจกรรม<br />1).ขโมยข้อมูลประจำตัว การจัดให้ข้อมูลเท็จหรือหมายเลขบัญชี<br />2).ใช้ช่องโหว่ทางเทคนิคและช่องโหว่ของกฏหมายเพื่อรับรางวัลเงินสด<br />3).การเข้าร่วมกิจะกรรมด้วยหลายบัญชีภายใต้ IP และอุปกรณ์เดียวกัน<br />4).การลงทะเบียนบัญชีเป็นชุด หรือการลงทะเบียนบัญชีไม่ใช่เพื่อวัตถุประสงค์ในการใช้แอป<br />5).พฤติกรรมอื่นๆที่เป็นอันตรายต่อชื่อเสียงหรือกฏหมายชุมชนของ Trading Live</p>\n<pre id=\"tw-target-text\" class=\"tw-data-text tw-text-large tw-ta\" dir=\"ltr\" data-placeholder=\"翻译\"><span class=\"Y2IQFc\" lang=\"th\">5.กิจกรรมนี้จำกัดเฉพาะผู้ใช้จากประเทศต่อไปนี้:\nซาอุดีอาระเบีย กาตาร์ อียิปต์ สหรัฐอาหรับเอมิเรตส์ มาเลเซีย สิงคโปร์ ไต้หวัน ฮ่องกง</span></pre>\n<p>สิทธิ์ในการตีความขั้นสุดท้ายของกิจกรรมเป็นของ Trading Live<br />หากคุณมีคำถามใดๆ โปรดส่งอีเมลไปที่service@trading.live</p>",
    "withdrawRule": "<p>1.หากรางวัลสะสมถึงเกณฑ์การถอนเงิน50ดอลล่าร์คุณสามารถเริ่มการถอนในหน้าบิล<br />2.หลังจากกรอกที่อยู่กระเป๋าเงินดิจิทัลและส่งใบสมัครอย่างถูกต้องแล้ว ผู้รับผิดชอบกิจกรรมจะเริ่มชำระเงินหลังจากการตรวจสอบและอนุมัติ<br />3.แจ้งเตือนชำระเงินจะส่งให้คุณโดยข้อความระบบและอีเมล โปรดให้ความสนใจรับ<br />4.หากคุณมีคำถามใดๆ โปรดติดต่อ service@trading.live</p>",
    "userInvitedPrize": "ลงทะเบียนและเข้าสู่ระบบจะได้รับสูงสุด30ดอลล่าร์!\\n การเปิดคำเชิญเพื่อนไม่จำกัด แนะนำมากขึ้น รับมากขึ้น!",
    "invitedPageAttention": "<p>1.รางวัลกิจกรรม: หลังจากลงทะเบียนและเข้าสู่ระบบแล้ว บัญชีสามารถได้รับเงินสูงสุด30ดอลล่าร์จากระบบ ผู้ใช้ที่ลงทะเบียนจะมีลิงก์คำเชิญพิเศษ หลังจากเพื่อนลงทะเบียนผ่านลิงก์พิเศษของคุณ คุณและผู้ได้รับเชิญสามารถได้รับเงินสูงสุด30ดอลล่าร์/ต่อคนจากระบบ ข้อมูลรายละเอียดจะขึ้นอยู่กับการแสดงบนหน้ากิจกรรม!</p>\n<p>2.การถอนรางวัล: ผู้ใช้ที่ถึงเกณฑ์การถอนเงินภายในเวลากิจกรรมสามารถเริ่มการถอนได้ในหน้าบิล</p>\n<p>3.คำเชิญที่ถูกต้อง: ผู้ใช้จริงที่ลงทะเบียนและเข้าสู่ระบบภายใต้ลิงก์พิเศษเป็นคำเชิญที่ถูกต้อง ผู้ใช้ลงทะเบียนจะได้รับคำเชิญไม่จำกัดทุกวัน แต่ผู้ใช้ลงทะเบียนซึ่งมีอีเมล/หมายเลขโทรศัพท์เดียวกันไม่สามารถเชิญจากผู้ใช้หลายคน ผู้ใช้จริงต้องเข้าสู่ระบบภายใต้ IP และอุปกรณ์เดียวกันจะเป็นบัญชีแรกเท่านั้น คำเชิญจะต้องเกิดขึ้นในเวลากิจกรรมและภายในพื้นที่กิจกรรม!</p>\n<p>4.ห้ามของกิจกรรมการละเมิด:&nbsp;<br />ผู้ใช้ไม่สามารถมีกิจกรรมที่ผิดกฏหมาย การละเมิด ผิดปกติหรือไม่เหมาะสม เมื่อเราพบ Trading Live จะมีสิทธิ์ตัดสิทธิ์จากการเข้าร่วมกิจกรรม<br />1).ขโมยข้อมูลประจำตัว การจัดให้ข้อมูลเท็จหรือหมายเลขบัญชี<br />2).ใช้ช่องโหว่ทางเทคนิคและช่องโหว่ของกฏหมายเพื่อรับรางวัลเงินสด<br />3).การเข้าร่วมกิจะกรรมด้วยหลายบัญชีภายใต้ IP และอุปกรณ์เดียวกัน<br />4).การลงทะเบียนบัญชีเป็นชุด หรือการลงทะเบียนบัญชีไม่ใช่เพื่อวัตถุประสงค์ในการใช้แอป<br />5).พฤติกรรมอื่นๆที่เป็นอันตรายต่อชื่อเสียงหรือกฏหมายชุมชนของ Trading Live</p>\n<p>สิทธิ์ในการตีความขั้นสุดท้ายของกิจกรรมเป็นของ Trading Live<br />หากคุณมีคำถามใดๆ โปรดส่งอีเมลไปที่service@trading.live</p>",
    "title": "null",
    "description": "null",
    "keyword": "null"
  },
  {
    "langId": 10,
    "appEntranceDesc": "Nhấp đây để bắt đầu kiếm USD ngay!",
    "name": "Mời bạn bè, nhận USD",
    "invitePrize": "Mời bạn bè đăng ký tài khoản Trading Live. \\nMời bạn bè nhiều hơn, nhận USD nhiều hơn!",
    "activityRuleSummary": "<p>Mời bạn b&egrave; đăng k&yacute; t&agrave;i khoản Trading Live. V&agrave; một khi bạn b&egrave; đăng nhập t&agrave;i khoản th&agrave;nh c&ocirc;ng, bạn v&agrave; bạn b&egrave; của bạn c&oacute; thể nhận tối đa 30 USD mỗi lần! Mời bạn b&egrave; nhiều hơn, nhận USD nhiều hơn!</p>",
    "activityRule": "<p>1. Phần thưởng: những người d&ugrave;ng đ&atilde; đăng k&yacute; sẽ c&oacute; thể lấy link mời bạn b&egrave;. Một khi bạn b&egrave; đăng k&yacute; t&agrave;i khoản th&agrave;nh c&ocirc;ng, bạn v&agrave; bạn b&egrave; của bạn đều sẽ c&oacute; cơ hội nhận phần thưởng tối đa 30 USD mỗi lần. Cụ thể, vui l&ograve;ng xem quy định tr&ecirc;n trang sự kiện.</p>\n<p>2. Mời bạn b&egrave; hữu hiệu: chỉ c&oacute; những người d&ugrave;ng thật đăng k&yacute; v&agrave; đăng nhập t&agrave;i khoản th&ocirc;ng qua link mời mới được coi l&agrave; hữu hiệu. Kh&ocirc;ng hạn chế số lượng mời bạn b&egrave;, nhưng những người d&ugrave;ng đăng k&yacute; qua một Email/ số điện thoại giống nhau chỉ c&oacute; thể được mời một lần. V&agrave; đối với những t&agrave;i khoản đăng k&yacute;/ đăng nhập với IP v&agrave; thiết bị thống nhất, th&igrave; chỉ c&oacute; t&agrave;i khoản đăng k&yacute; đầu tư l&agrave; hữu hiệu. Chỉ những việc mời bạn b&egrave; v&agrave;o thời gian sự kiện v&agrave; trong những khu vực được ph&eacute;p tham gia sự kiện mới được coi l&agrave; hữu hiệu.</p>\n<p>3. R&uacute;t tiền thưởng: Trong thời gian sự kiện, khi số tiền thường đạt điều kiện r&uacute;t tiền, th&igrave; người d&ugrave;ng c&oacute; thể thực hiện r&uacute;t tiền tại trang chi tiết.</p>\n<p>4. Những h&agrave;nh động vi phạm:<br />Người d&ugrave;ng kh&ocirc;ng thể xuất hiện c&aacute;c h&agrave;nh vi vi phạm, kh&aacute;c thường hoặc kh&ocirc;ng ch&iacute;nh đ&aacute;ng. Một khi ph&aacute;t hiện, th&igrave; Trading Live cẽ c&oacute; thể hủy tư c&aacute;ch tham gia sự kiện của những người d&ugrave;ng tương ứng.<br />1). Đ&aacute;nh cấp danh tiếng, cung cấp th&ocirc;ng tin hoặc t&agrave;i khoản sai sự thật;<br />2). Th&ocirc;ng qua lỗ hổng kỹ thuật, hoặc lỗ hổng quy tắc, để nhận tiền thưởng &aacute;c &yacute;;&nbsp;<br />3). Tham gia hoạt động qua nhiều t&agrave;i khoản với một IP v&agrave; thiết bị;<br />4). Đăng k&yacute; hoặc nu&ocirc;i t&agrave;i khoản số lượng lớn, hoặc v&igrave; mục đ&iacute;ch kh&ocirc;ng sử dụng App;<br />5). Những h&agrave;nh động l&agrave;m thiệt hại danh tiếng hoặc quy tắc cộng của Trading Live.</p>\n<p>5. Sự kiện n&agrave;y chỉ d&agrave;nh cho người d&ugrave;ng từ c&aacute;c quốc gia sau: Ả Rập Saudi, Qatar, Ai Cập, C&aacute;c Tiểu vương quốc Ả Rập Thống nhất, Malaysia, Singapore, Đ&agrave;i Loan v&agrave; Hồng K&ocirc;ng.</p>\n<p>Quyền giải th&iacute;ch sự kiện cuối c&ugrave;ng thuộc về Trading Live, nếu bạn c&oacute; bất kỳ c&acirc;u hỏi n&agrave;o vui l&ograve;ng gửi Email tới: service@trading.live</p>",
    "withdrawRule": "<p>1. Khi số tiền thưởng đạt tới mức 50 USD, th&igrave; bạn sẽ được ph&eacute;p r&uacute;t tiền.<br />2. Điền đ&uacute;ng địa chỉ V&iacute; v&agrave; c&aacute;c th&ocirc;ng tin cần thiết, v&agrave; gửi đơn xin r&uacute;t tiền. V&agrave; nh&acirc;n vi&ecirc;n sẽ x&eacute;t duyệt đơn xin r&uacute;t tiền của bạn. V&agrave; một khi được th&ocirc;ng qua x&eacute;t duyệt, th&igrave; ch&uacute;ng t&ocirc;i sẽ chuyển tiền cho bạn.<br />3. Th&ocirc;ng b&aacute;o thanh to&aacute;n sẽ gửi cho bạn qua thống b&aacute;o hệ thống v&agrave; Email. Xin lưu &yacute; kiểm tra.<br />4. Nếu bạn c&oacute; vấn đề g&igrave;, xin li&ecirc;n hệ qua Email: service@trading.live</p>",
    "userInvitedPrize": "Đăng ký tài khoản nhận tối đa 30 USD! \\nMời bạn bè để nhận tiền thưởng thêm!\\n Mời bạn bè nhiều hơn, nhận USD nhiều hơn!",
    "invitedPageAttention": "<p>1. Phần thưởng: Đăng k&yacute; t&agrave;i khoản nhận tối đa 30 USD! V&agrave; những người d&ugrave;ng đ&atilde; đăng k&yacute; sẽ c&oacute; thể lấy link mời bạn b&egrave;. Một khi bạn b&egrave; đăng k&yacute; t&agrave;i khoản th&agrave;nh c&ocirc;ng th&ocirc;ng qua link mời của bạn, bạn v&agrave; bạn b&egrave; của bạn sẽ c&oacute; cơ hội nhận phần thưởng tối đa 30 USD mỗi lần. Cụ thể, vui l&ograve;ng xem quy định tr&ecirc;n trang sự kiện.</p>\n<p>2. Mời bạn b&egrave; hữu hiệu: chỉ c&oacute; những người d&ugrave;ng thật đăng k&yacute; v&agrave; đăng nhập t&agrave;i khoản th&ocirc;ng qua link mời mới được coi l&agrave; hữu hiệu. Kh&ocirc;ng hạn chế số lượng mời bạn b&egrave;, nhưng những người d&ugrave;ng đăng k&yacute; qua một Email/ số điện thoại giống nhau chỉ c&oacute; thể được mời một lần. V&agrave; đối với những t&agrave;i khoản đăng k&yacute;/ đăng nhập với IP v&agrave; thiết bị thống nhất, th&igrave; chỉ c&oacute; t&agrave;i khoản đăng k&yacute; đầu tư l&agrave; hữu hiệu. Chỉ những việc mời bạn b&egrave; v&agrave;o thời gian sự kiện v&agrave; trong những khu vực được ph&eacute;p tham gia sự kiện mới được coi l&agrave; hữu hiệu.</p>\n<p>3. R&uacute;t tiền thưởng: Trong thời gian sự kiện, khi số tiền thường đạt điều kiện r&uacute;t tiền, th&igrave; người d&ugrave;ng c&oacute; thể thực hiện r&uacute;t tiền tại trang chi tiết.</p>\n<p>4.Những h&agrave;nh động vi phạm:<br />Người d&ugrave;ng kh&ocirc;ng thể xuất hiện c&aacute;c h&agrave;nh vi vi phạm, kh&aacute;c thường hoặc kh&ocirc;ng ch&iacute;nh đ&aacute;ng. Một khi ph&aacute;t hiện, th&igrave; Trading Live cẽ c&oacute; thể hủy tư c&aacute;ch tham gia sự kiện của những người d&ugrave;ng tương ứng.<br />1). Đ&aacute;nh cấp danh tiếng, cung cấp th&ocirc;ng tin hoặc t&agrave;i khoản sai sự thật;<br />2). Th&ocirc;ng qua lỗ hổng kỹ thuật, hoặc lỗ hổng quy tắc, để nhận tiền thưởng &aacute;c &yacute;;&nbsp;<br />3). Tham gia hoạt động qua nhiều t&agrave;i khoản với một IP v&agrave; thiết bị;<br />4). Đăng k&yacute; hoặc nu&ocirc;i t&agrave;i khoản số lượng lớn, hoặc v&igrave; mục đ&iacute;ch kh&ocirc;ng sử dụng App;<br />5). Những h&agrave;nh động l&agrave;m thiệt hại danh tiếng hoặc quy tắc cộng của Trading Live.</p>\n<p>Quyền giải th&iacute;ch sự kiện cuối c&ugrave;ng thuộc về Trading Live, nếu bạn c&oacute; bất kỳ c&acirc;u hỏi n&agrave;o vui l&ograve;ng gửi Email tới: service@trading.live</p>",
    "title": "null",
    "description": "null",
    "keyword": "null"
  },
  {
    "langId": 12,
    "appEntranceDesc": "简中-点击立即开始赚取USD!",
    "name": "邀好友，赚USD！",
    "invitePrize": "邀好友注册Trading Live，邀得越多，赚得越多！",
    "activityRuleSummary": "<p>邀好友注册并登录Trading Live，你和你的好友可同时获得系统赠送的最高30USD每人次！邀得越多，赚得越多！</p>",
    "activityRule": "<p>1. 活动奖励：已注册用户拥有专属邀约链接，好友通过你的专属链接注册后，你和被邀约人可以同时获得系统随机的最高30USD 的奖励金每人次，具体以活动页面显示为准。</p>\n<p>2. 有效邀请：通过专属链接下注册并登陆的真实用户才算有效邀约。注册用户每天邀约不受限制，同一邮箱/手机号注册用户不可以被多个用户邀约。同一IP和设备下登录的有效用户有且只算首个账号。邀请必须是在活动时间，活动地区内发生。</p>\n<p>3. 奖励提现：用户在活动时间内达到提现门槛的可以在账单页面发起提现。</p>\n<p>4. 违规行为的禁止：<br />用户不得从事任何违规，异常或者不正当行为，一旦发现，Trading Live将有权取消其参与活动的资格。<br />1). 盗用身份，提供虚假信息或者账号的<br />2). 利用技术漏洞，规则漏洞，恶意获取现金奖励；<br />3). 同一IP和设备下多账号参与活动；<br />4). 批量或非出于APP使用目的的注册账号，养号；<br />5). 其他危害Trading Live名誉或者社区守则的行为<br /><br /><br /></p>\n<p>活动最终解释权归Trading Live所有，如果有任何疑问请邮件至service@trading.live</p>",
    "withdrawRule": "<p>1. 奖励累计到提现门槛50USD的可以在账单页面发起提现。<br />2. 准确填写数字钱包地址提交申请后，活动负责人员审核通过后将会发起打款。<br />3. 已打款通知会通过系统消息和邮件的形式发送。请注意查收<br />4. 任何问题请联系service@trading.live</p>",
    "userInvitedPrize": "注册登录立得最高30USD每人次！开启无限邀好友，邀得越多，赚得越多！",
    "invitedPageAttention": "<p>1. 活动奖励：通过好友邀请注册登录后，账户将到账系统随机的最高30USD 的奖励金。同时已注册用户拥有专属邀约链接，好友通过你的专属链接注册后，你和被邀约人可以同时获得系统随机的最高30USD 的奖励金每人次，具体以活动页面显示为准。</p>\n<p>2. 奖励提现：用户在活动时间内达到提现门槛的可以在账单页面发起提现。</p>\n<p>3. 有效邀请：通过专属链接下注册并登陆的真实用户才算有效邀约。注册用户每天邀约不受限制，同一邮箱/手机号注册用户不可以被多个用户邀约。同一IP和设备下登陆的有效用户有且只算首个账号。邀请必须是在活动时间，活动地区内发生。</p>\n<p>4. 违规行为的禁止：<br />用户不得从事任何违规，异常或者不正当行为，一旦发现, Trading Live将有权取消其参与活动的资格。<br />1). 盗用身份，提供虚假信息或者账号的;<br />2). 利用技术漏洞，规则漏洞，恶意获取现金奖励；<br />3). 同一IP和设备下多账号参与活动；<br />4). 批量或非出于APP使用目的的注册账号，养号；<br />5). 其他危害Trading Live名誉或者社区守则的行为。<br /><br /></p>\n<p>活动最终解释权归Trading Live所有，如果有任何疑问请邮件至service@trading.live</p>",
    "title": "",
    "description": "",
    "keyword": ""
  },
  {
    "langId": 13,
    "appEntranceDesc": "印尼-Klik untuk mulai menghasilkan USD sekarang!",
    "name": "Undang teman dan dapatkan USD!",
    "invitePrize": "Undang teman untuk mendaftar Trading Live, semakin banyak Anda mengundang, semakin banyak penghasilan Anda!",
    "activityRuleSummary": "<p>Undang teman Anda untuk mendaftar dan masuk ke Trading Live, dan Anda dan teman Anda bisa mendapatkan hingga 30USD per orang secara bersamaan! Semakin banyak Anda mengundang, semakin banyak penghasilan Anda!</p>",
    "activityRule": "<p>1. Hadiah acara: Pengguna terdaftar memiliki tautan undangan eksklusif, dan setelah teman mendaftar melalui tautan eksklusif Anda, Anda dan orang yang diundang dapat secara bersamaan menerima hadiah acak hingga 30USD per orang per orang, tergantung pada tampilan di halaman acara.2. Undangan yang valid: Hanya pengguna asli yang mendaftar dan masuk melalui tautan eksklusif yang dianggap sebagai undangan yang valid. Tidak ada batasan undangan harian pengguna terdaftar, dan pengguna terdaftar dengan alamat email/nomor ponsel yang sama tidak dapat diundang oleh banyak pengguna. Pengguna yang valid masuk dengan alamat IP dan perangkat yang sama memiliki dan hanya dihitung sebagai akun pertama. Undangan harus dilakukan pada waktu acara, di dalam area acara.3. Penarikan hadiah: Pengguna yang mencapai ambang penarikan selama periode acara dapat memulai penarikan di halaman penagihan.4. Larangan Pelanggaran:Pengguna tidak boleh terlibat dalam perilaku yang tidak teratur, abnormal atau tidak pantas dan Trading Live berhak untuk mendiskualifikasi mereka dari berpartisipasi dalam Promosi.1). Mencuri identitas, memberikan informasi palsu atau nomor rekening2). Memanfaatkan celah teknis dan celah aturan untuk mendapatkan hadiah uang tunai dengan jahat;3). Beberapa akun di bawah IP dan perangkat yang sama untuk berpartisipasi dalam aktivitas;4). Penggunaan batch atau non-APP dari akun terdaftar, akun pemeliharaan;5) Tindakan lain yang membahayakan reputasi Trading Live atau Peraturan KomunitasInterpretasi akhir dari acara ini adalah milik Trading Live, jika Anda memiliki pertanyaan, silakan email service@trading.live</p>",
    "withdrawRule": "<p>1. Jika reward telah terakumulasi ke ambang penarikan sebesar 50USD, Anda dapat melakukan penarikan di halaman penagihan.2. Setelah mengisi alamat dompet digital secara akurat dan mengirimkan aplikasi, penanggung jawab aktivitas akan melakukan pembayaran setelah peninjauan disetujui.3. Pemberitahuan pembayaran berbayar akan dikirim melalui pesan sistem dan email. Harap perhatikan cek4. Silakan hubungi service@trading.live untuk pertanyaan apa pun</p>",
    "userInvitedPrize": "Daftar dan log up to 30USD per orang! Aktifkan undangan teman tanpa batas, semakin banyak Anda mengundang, semakin banyak penghasilan Anda!",
    "invitedPageAttention": "<p>1. Hadiah Acara: Setelah mendaftar dan masuk melalui undangan teman, akun akan dikreditkan ke sistem dengan hadiah acak hingga 30USD. Pada saat yang sama, pengguna terdaftar memiliki tautan undangan eksklusif, setelah teman mendaftar melalui tautan eksklusif Anda, Anda dan orang yang diundang bisa mendapatkan hadiah acak hingga 30USD per orang pada saat yang sama, tergantung pada tampilan di halaman acara.2. Penarikan hadiah: Pengguna yang mencapai ambang penarikan selama periode kampanye dapat memulai penarikan di halaman penagihan.3. Undangan yang valid: Hanya pengguna nyata yang mendaftar dan masuk melalui tautan eksklusif yang dianggap sebagai undangan yang valid. Tidak ada batasan undangan harian pengguna terdaftar, dan pengguna terdaftar dengan alamat email/nomor ponsel yang sama tidak dapat diundang oleh banyak pengguna. Pengguna valid yang masuk dengan alamat IP dan perangkat yang sama memiliki dan hanya dihitung sebagai akun pertama. Undangan harus dilakukan pada waktu acara, di dalam area acara.4. Larangan Pelanggaran:Pengguna tidak boleh terlibat dalam perilaku yang tidak teratur, tidak biasa atau tidak pantas dan Trading Live berhak untuk mendiskualifikasi mereka dari berpartisipasi dalam Promosi.1) Mencuri identitas, memberikan informasi palsu atau nomor rekening;2). Memanfaatkan celah teknis dan celah aturan untuk mendapatkan hadiah uang tunai dengan jahat;3). Beberapa akun di bawah IP dan perangkat yang sama untuk berpartisipasi dalam aktivitas;4). Penggunaan batch atau non-APP dari akun terdaftar, akun pemeliharaan;5) Tindakan lain yang membahayakan reputasi Trading Live atau Peraturan Komunitas.Interpretasi akhir dari acara ini adalah milik Trading Live, jika Anda memiliki pertanyaan, silakan email service@trading.live</p>",
    "title": "null",
    "description": "null",
    "keyword": "null"
  }
],
  "config":
{
  "peopleLimitType": 0,
  "peopleLimitCount": "null",
  "timeDayLimit": "null",
  "timePeopleLimit": "null",
  "userLoginTime": "null",
  "userActiveCount": "null",
  "withdrawLimit": "null",
  "deviceLimit": "null"
},
"countryList": [],
"endTime": 1685548799000,
"id": 182,
"mobileUrl": "https://testfbeventwap.tostar.top",
"otherConfig": "string",
"positionList": [4,13],
"productId": 0,
"putCountryType": 0,
"relateUserPrize":{
  "prizeType": "USD",
  "prizeAmountType": 0,
  "prizeFixAmount": "20",
  "prizeRandomAmountMin": "null",
  "prizeRandomAmountMax": "null",
  "randomPrize": [
    {
      "min": "",
      "max": "",
      "ratio": ""
    }
  ]
},
"shareLogo": "string",
"startTime": 1681833600000,
"status": 1,
"taskId": 1,
"timeZone": "string",
"userPrize": {
  "prizeType": "USD",
  "prizeAmountType": 0,
  "prizeFixAmount": 30,
  "prizeRandomAmountMin": "null",
  "prizeRandomAmountMax": "null",
  "randomPrize": [
    {
      "min": "null",
      "max": "null",
      "ratio": "null"
    }
  ]
},
"webUrl": "string"
}


