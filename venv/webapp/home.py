import justpy as jp


class Home:
    path = '/'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text='This is the Home page!',
               classes='text-5xl p-2')
        jp.Div(a=div, text='Socioemotional Selectivity Theory Throughout the Lifespan',
               classes='text-center text-3xl text-blue-500')
        jp.Div(a=div, text="""
                While aging is often associated with loss and infirmness, socioemotional selectivity theory
                indicates that there are positive benefits to aging. The theory is based on the idea that
                humans change their goals as they age due to the uniquely human ability to understand time.
                Thus, when people are young adults and see time as open-ended, they prioritize goals that focus on
                the future, such as learning new information and expanding their horizons through activities
                like travel or enlarging their social circle. Yet, as people grow older and perceive
                their time as more constrained, their goals shift to become more focused on emotional
                gratification in the present. This leads people to prioritize experiences that
                are meaningful, such as deepening relationships with close friends and family and savoring
                favorite experiences. It’s important to understand that as much as socioemotional selectivity
                theory tends to emphasize age-related changes in goals, those changes aren’t the result of
                chronological age per se. Instead, they come about because of people’s perceptions
                of the time they have left. Because people perceive their time dwindling as they age,
                adult age differences are the easiest way to see socioemotional selectivity
                theory at work. However, people’s goals may shift in other situations too.
                For example, if a young adult becomes terminally ill, their goals will shift
                as their time is truncated. Similarly, if one knows a specific set of circumstances
                is coming to an end, their goals may shift as well. For instance, if one is planning to
                move out of state, as the time of their departure draws closer, they will be more
                likely to spend time cultivating the relationships that matter most to them
                while worrying less about expanding their network of acquaintances in the town
                they will be leaving. Thus, socioemotional selectivity theory demonstrates that the human ability
                to perceive time impacts motivation. Whereas the pursuit of long-term rewards makes sense
                when one perceives their time as expansive, when time is perceived as limited,
                emotionally fulfilling and meaningful goals take on new relevance.
                As a result, the shift in goals as time horizons change outlined by socioemotional selectivity
                theory is adaptive, enabling people to focus on longer term work and family goals
                when they’re young and achieving emotional gratification as they get older.
                """, classes='text-lg text-stone-800')

        return wp
