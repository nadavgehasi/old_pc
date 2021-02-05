package hello

import hello.world.helloWorld
import org.junit.jupiter.api.Test
import kotlin.test.assertEquals

class HelloWorldTest {

    @Test
    fun helloWorldTest() {
        assertEquals("Hello world", helloWorld())
    }
}