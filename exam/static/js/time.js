function showtime(ts) {
                            var timerun = false; //是否启用
                            var Temp; //输出字符串
                            var tempts = ts - 1; //剩余秒数-1
                            var startTime = (new Date()).getTime(); //当前时间
                            var dateLeft = 0; //剩余天数
                            var hourLeft = 0; //剩余小时
                            var minuteLeft = 0; //剩余分钟
                            var secondLeft = 0; //剩余秒钟

                            var dateLeftStr = '';//剩余天数字符
                            var hourLeftStr = '';//剩余小时字符
                            var minuteLeftStr = '';//剩余分钟字符
                            var secondLeftStr = '';//剩余秒钟字符
                            if (ts < 0)//剩余秒数为负则全部清0
                            {
                                ts = 0;
                                dateLeft = 0;
                                hourLeft = 0;
                                minuteLeft = 0;
                                secondLeft = 0;
                            }
                            else {

                                dateLeft = parseInt(ts / 86400); //折合天数
                                ts = ts - dateLeft * 86400; //剩余秒数
                                hourLeft = parseInt(ts / 3600); //折合小时
                                ts = ts - hourLeft * 3600; //剩余秒数
                                minuteLeft = parseInt(ts / 60); //折合分钟
                                secondLeft = ts - minuteLeft * 60; //剩余秒数

                                dateLeftStr = dateLeft;
                                hourLeftStr = hourLeft;
                                minuteLeftStr = minuteLeft;
                                secondLeftStr = secondLeft;
                            }
                            if (hourLeft < 10)
                                hourLeftStr = '0' + hourLeft; //小时左补0
                            if (minuteLeft < 10)
                                minuteLeftStr = '0' + minuteLeft; //分钟左补0
                            if (secondLeft < 10)
                                secondLeftStr = '0' + secondLeft; //秒钟左补0
                            if (dateLeft > 0)
                                //天数> 0，显示天数
                                dateLeftStr = dateLeftStr + '天 ';
                            else
                                //否则不显示天数
                                dateLeftStr = " ";
                            if (hourLeft > 0)
                                //小时> 0，显示小时数
                                hourLeftStr = hourLeftStr + '小时 ';
                            else {
                                //否则判断天数是否也为0
                                if (dateLeft != " ")//天数不为0
                                    hourLeftStr = "00" + '小时 '; //显示小时数为00
                                else
                                    hourLeftStr = " "; //否则不显示小时数
                            }
                            if (minuteLeft > 0)//分钟是否为0
                                minuteLeftStr = minuteLeftStr + '分钟 '; //显示分钟
                            else {
                                if (dateLeft != " " || hourLeft != " ")
                                    minuteLeftStr = "00" + '分钟 '; //天数和小时有一个不为0则显示00分钟
                                else
                                    minuteLeftStr = " "; //否则不显示分钟
                            }
                            if (secondLeft > 0)
                                //秒钟是否为0
                                secondLeftStr = secondLeftStr + '秒 '; //不为0显示秒
                            else {
                                if (dateLeftStr != " " || hourLeftStr != " " || minuteLeftStr != " ")
                                    secondLeftStr = "00" + '秒 '; //天数、小时、分钟有一个不为0则显示00秒
                                else
                                    secondLeftStr = " "; //否则不显示秒
                            }
                            Temp = dateLeftStr + hourLeftStr + minuteLeftStr + secondLeftStr; //合并字符串
                            if (Temp == ' ') {
                                Temp = " <B>结束</B> "; //时间到停止倒计时
                            }
                            else {
                                Temp = "" + Temp;
                                timerun = true;
                            }
                            document.getElementById("datetime").innerHTML = Temp;
                            if (timerun)//继续倒计时
                                setTimeout('showtime( ' + tempts + ') ', 1000);

                        }