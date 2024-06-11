rm -rf /tmp/.server*
valipar inst -p TokenRingMaster TokenRingSlave TokenRingSlave -f Buffer.class Producer.class TokenRingMaster.class TokenRingSlave.class -i ValiparInitializer.class
