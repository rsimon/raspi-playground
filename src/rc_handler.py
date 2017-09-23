'''
The server-side component handling the remote
control Web socket connection
'''
class RemoteControlHandler(WebSocket):

    '''
    def proximity_polling(conn):
        count = 0
        while count < 5:
            time.sleep(2)
            count += 1
            conn.send("Yay!")
    '''

    def opened(self):
        self.servo = GPIO.PWM(23, 50)
        self.servo.start(7.5)

        '''
        # TODO start proximity sensor thread
        t = threading.Thread(target = self.proximity_polling)
        t.start()
        '''

    def received_message(self, message):
        # Heading is a value between 0 and 100
        if (message.data.startswith('heading')):
            heading = float(message.data[8:])
            dutyCycle = 2.5 + 10.5 * heading / 100
            self.servo.ChangeDutyCycle(dutyCycle)
