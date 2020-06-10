import pprint

message = ''' Hà Nội, ngày 26 tháng 2 năm 2020



Dạo này mất ngủ và hay suy nghĩ lung tung thấy cuộc sống bộn bề nhiều lo toan quá. Buổi sáng mở mắt ra chào buổi sáng bằng một tinh thần không thực sự tốt nhưng cơ bản vẫn thấy vui vì mình còn được sống còn thở,... Lướt facebook mới nhớ nay thứ 4, bắt đầu mùa chay và ăn chay. Hôm qua đi uống trà sữa với bạn gấu mà tối về bị kiểu cồn ruột mất ngủ luôn.

Lấy đà mãi cuối cùng cũng bò dậy, mở máy tính gửi cái CVcho mấy bạn HR. Từ khung cửa sổ, dãy nhà đối diện vẫn im lìm, con ngõ vắng lặng bỗng náo nhiệt với tiếng hét của lũ trẻ nghỉ học vì cúm corona, bật bản nhạc đã từ rất lâu rồi không nghe từ những ngày nghỉ việc. Một cảm giác hết sức bình yên, không cảm thấy cồn cào da diết như những ngày xưa cũ, nhớ bạn crush ngày xưa bất giác mỉm cười. Âm nhạc ở giây phút ấy đã theo những kẻ hở vô hình nào đó ăn sâu vào tiềm thức bị đánh thức, một cô gái rất vui vẻ ngày xưa, một cô gái đầy muộn phiền và xao xuyến và giờ một cô gái dường như chỉ cần an nhiên với cuộc đời. Mình vẫn nhớ mãi những tháng ngày mà mình cả ngày chỉ nghe bài hát "Mùa thu lá xanh" và mình đọc được ở đâu đó một câu như này "Cái kết tốt nhất với một kẻ đơn phương là tìm được một người thương mình thật lòng và kẻ đó cũng thương người đó". ừ, chậc chắc là đúng.





Gần đây, mình có nhận lời làm người yêu một bạn vì sao thì mình cũng chịu, cũng nhớ cũng thương nhưng cũng vẫn tự hỏi lòng đó có phải là yêu. 28 tuổi, cũng từng trải qua rất nhiều cảm xúc nhưng thực sự vẫn mông lung trong khái niệm tình yêu. Có phải tình yêu là tìm thấy sự an nhiên khi ở bên một người, có người cho bạn mượn bờ vai một chiều hồ Tây hay những lúc yếu lòng? Là người mà bạn có thể nói tất cả nỗi lòng, nỗi lo lắng ? Nhưng liệu nếu đó là tình yêu thì tình yêu có hạn sử dụng không? Thật ra thì tất cả những thứ bên trên chỉ là những thứ mà bản thân mình không nắm rõ, không am hiểu cũng không thể nào kiểm soát. Thứ mình có thể kiểm soát chỉ là bản thân mình, suy nghĩ tích cực yêu quý cuộc sống và tận hưởng từng giây phút an nhiên của đời mình một các thật trọn vẹn....



                Gửi vào âm thanh vắng lặng kia những muộn phiền, âu lo để bình yên đâu đó lại trở về bên ta.'''             
count = {}

for character in message:
	count.setdefault(character,0)
	count[character]+=1

pprint.pprint(count)