using NUnit.Framework;
using ServiceStack;
using ServiceStack.Testing;
using MyApp.ServiceInterface;
using MyApp.ServiceModel;

namespace MyApp.Tests
{
    public class UnitTest
    {
        private readonly ServiceStackHost appHost;

        public UnitTest()
        {
            appHost = new BasicAppHost().Init();
            appHost.Container.AddTransient<MyServices>();
        }

        [OneTimeTearDown]
        public void OneTimeTearDown() => appHost.Dispose();

        [Test]
        public void Can_call_MyServices()
        {
            var service = appHost.Container.Resolve<MyServices>();

            var response = (HelloResponse)service.Any(new Hello { Name = "World" });

            Assert.That(response.Result, Is.EqualTo("Hello, World!"));
        }

        [Test]
        public void Can_render_home_page()
        {
            var service = appHost.Container.Resolve<MyServices>();

            var response = service.Any(new Hello { Name = "Home" });

            Assert.That(response.Result, Is.EqualTo("Hello, Home!"));
        }

        [Test]
        public void Home_page_renders_quickly()
        {
            var service = appHost.Container.Resolve<MyServices>();

            var stopwatch = new System.Diagnostics.Stopwatch();
            stopwatch.Start();

            var response = service.Any(new Hello { Name = "Home" });

            stopwatch.Stop();

            Assert.That(stopwatch.ElapsedMilliseconds, Is.LessThan(200));
        }
    }
}
