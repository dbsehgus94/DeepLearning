import tensorflow as tf

# 플레이스홀더 정의하기
a = tf.placeholder(tf.int32, [3]) # 정수 자료형 3개를 가진 배열

# 배열을 모든 값을 2배하는 연산 정의하기
b = tf.constant(2);
x2_op = a * b;

c = tf.constant([1, 2, 3])
print(c)
float_tensor = tf.cast(tf.constant([1, 2, 3]), dtype = tf.float32)
print(float_tensor)


# 세션 시작하기
sess = tf.Session()

# 플레이스홀더에 값을 넣고 실행하기
r1 = sess.run(x2_op, feed_dict={ a: [1, 2, 3]})
print(r1)
r2 = sess.run(x2_op, feed_dict={ a : [10, 20, 10]})
print(r2)

