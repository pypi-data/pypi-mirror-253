import discord 
from discord.ext import commands
import sys
import typing
import pkg_resources
from ..core.work.types import ContextA
from ..core.codeblocks import Codeblock, codeblock_converter
import traceback
import math
import itertools
import time
from urllib.parse import urlencode
import asyncio
import io
import os, json
from datetime import datetime, timezone
import logging


from jejudo.modules import ExtensionConverter
from jejudo.shell import ShellReader
from jejudo.exception_handling import ReplResponseReactor
from jejudo.flags import Flags
from jejudo.paginators import PaginatorInterface, WrappedPaginator, use_file_check
from jejudo.functools import AsyncSender
from jejudo.repl import AsyncCodeExecutor, Scope, all_inspections, disassemble, get_var_dict_from_ctx

Directory = os.path.dirname(os.path.realpath(__file__))
logger: logging.Logger = logging.getLogger(__name__)

# ==============================================================================

try:
    import psutil
except ImportError:
    psutil = None

try:
    from importlib.metadata import distribution, packages_distributions
except ImportError:
    from importlib_metadata import distribution, packages_distributions

# ==============================================================================





def natural_size(size_in_bytes: int) -> str:
    """
    Converts a number of bytes to an appropriately-scaled unit
    E.g.:
        1024 -> 1.00 KiB
        12345678 -> 11.77 MiB
    """
    units = ('B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB')

    power = int(math.log(max(abs(size_in_bytes), 1), 1024))

    return f"{size_in_bytes / (1024 ** power):.2f} {units[power]}"


def natural_time(time_in_seconds: float) -> str:
    """
    Converts a time in seconds to a 6-padded scaled unit
    E.g.:
        1.5000 ->   1.50  s
        0.1000 -> 100.00 ms
        0.0001 -> 100.00 us
    """
    units = (
        ('mi', 60),
        (' s', 1),
        ('ms', 1e-3),
        ('\N{GREEK SMALL LETTER MU}s', 1e-6),
    )

    absolute = abs(time_in_seconds)

    for label, size in units:
        if absolute > size:
            return f"{time_in_seconds / size:6.2f} {label}"

    return f"{time_in_seconds / 1e-9:6.2f} ns"


def mean_stddev(collection: typing.Collection[float]) -> typing.Tuple[float, float]:
    """
    Takes a collection of floats and returns (mean, stddev) as a tuple.
    """

    average = sum(collection) / len(collection)

    if len(collection) > 1:
        stddev = math.sqrt(sum(math.pow(reading - average, 2) for reading in collection) / (len(collection) - 1))
    else:
        stddev = 0.0

    return (average, stddev)


def format_stddev(collection: typing.Collection[float]) -> str:
    """
    Takes a collection of floats and produces a mean (+ stddev, if multiple values exist) string.
    """
    if len(collection) > 1:
        average, stddev = mean_stddev(collection)

        return f"{natural_time(average)} \N{PLUS-MINUS SIGN} {natural_time(stddev)}"

    return natural_time(sum(collection) / len(collection))


class Dropdown(discord.ui.Select):
    def __init__(self, bot_: discord.Bot, requester,start_time):
        self.bot = bot_
        self.requester = requester
        self.start_time = start_time

        options = [
            discord.SelectOption(
                label="jejudo page", description="View the Jeju Island main page.", emoji="🟥"
            ),
            discord.SelectOption(
                label="protected_access page", description="The page related to the intent.", emoji="🟩"
            )
        ]

        super().__init__(
            placeholder="jejudo !! Click here to open the menu!",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        if interaction.user != self.requester:
            return await interaction.response.send_message("❌ jejudo is an owner-only command. !!", ephemeral=True)

        if self.values[0] == "jejudo page":

            jejudo = [
                f"> the, jejudo ` v{pkg_resources.get_distribution('jejudo').version} `, py-cord ` v{pkg_resources.get_distribution('py-cord').version} `".replace("\n", ""),
                f"ㄴ • Python ` {sys.version}`".replace("\n", ""),
                f"ㄴ • platform `{sys.platform}` • start loaded <t:{self.start_time.timestamp():.0f}:R>".replace("\n", "")
            ]
            
            if psutil:
                try:
                    proc = psutil.Process()

                    with proc.oneshot():
                        try:
                            mem = proc.memory_full_info()
                            jejudo.append(f"\n • {natural_size(mem.rss)} memory , {natural_size(mem.vms)} memory , {natural_size(mem.uss)} memory")
                        except psutil.AccessDenied:
                            pass

                        try:
                            name = proc.name()
                            pid = proc.pid
                            thread_count = proc.num_threads()

                            jejudo.append(f"ㄴ • PID {pid} (`{name}`) == {thread_count} thread(s)")
                        except psutil.AccessDenied:
                            pass

                        jejudo.append("")
                except psutil.AccessDenied:
                    jejudo.append(
                        "ㄴ • psutil is installed, but this process does not have high enough access rights "
                    )
                    jejudo.append("")

            cache_summary = f"` 🌐 {len(self.bot.guilds)} ` guild(s) ㅣ ` 🤴 {len(self.bot.users)} ` user(s)"

            if isinstance(self.bot, discord.AutoShardedClient):
                if len(self.bot.shards) > 20:
                    jejudo.append(
                        f"This bot is auto shards (` {len(self.bot.shards)} ` shards of ` {self.bot.shard_count} `)"
                        f"\n{cache_summary}."
                    )
                else:
                    shard_ids = ', '.join(str(i) for i in self.bot.shards.keys())
                    jejudo.append(
                        f"This bot is auto shards (Shards ` {shard_ids} ` of ` {self.bot.shard_count} `)"
                        f"\n{cache_summary}."
                    )
            elif self.bot.shard_count:
                jejudo.append(
                    f"This bot is manually sharded (Shard ` {self.bot.shard_id} ` of ` {self.bot.shard_count} `)"
                    f"\n{cache_summary}."
                )
            else:
                jejudo.append(f"This bot is not sharded\n{cache_summary}.")

            jejudo.append(f"\n\nAverage websocket latency: {round(self.bot.latency * 1000, 2)}ms")

            await interaction.response.edit_message(
                content="\n".join(jejudo)
            )
        if self.values[0] == "protected_access page":
            jejudo = [
                f"> the, jejudo ` v{pkg_resources.get_distribution('jejudo').version} `, py-cord ` v{pkg_resources.get_distribution('py-cord').version} `".replace("\n", ""),
                f"ㄴ • Python ` {sys.version}`".replace("\n", ""),
                f"ㄴ • platform `{sys.platform}` • start loaded <t:{self.start_time.timestamp():.0f}:R>".replace("\n", "")
            ]

            if self.bot._connection.max_messages:
                message_cache = f"Message cache capped at {self.bot._connection.max_messages}"
            else:
                message_cache = "Message cache is disabled"

            if discord.version_info >= (1, 5, 0):
                remarks = {
                    True: 'enabled',
                    False: 'disabled',
                    None: 'unknown'
                }

                *group, last = (
                    f"{intent.replace('_', ' ')} intent is {remarks.get(getattr(self.bot.intents, intent, None))}\n"
                    for intent in
                    ('presences', 'members', 'message_content')
                )

                jejudo.append(f"\n{message_cache}\n{''.join(group)}\n{last}")
            else:
                guild_subscriptions = f"guild subscriptions are {'enabled' if self.bot._connection.guild_subscriptions else 'disabled'}"  # type: ignore

                jejudo.append(f"\n{message_cache}\n{guild_subscriptions}")
            jejudo.append(f"Average websocket latency: {round(self.bot.latency * 1000, 2)}ms")

            await interaction.response.edit_message(
                content="\n".join(jejudo)
            )

class DropdownView(discord.ui.View):
    def __init__(self, bot_: discord.Bot, requester, start_time):
        self.bot = bot_
        self.requester = requester
        self.start_time = start_time
        super().__init__()
        self.add_item(Dropdown(self.bot, self.requester, self.start_time))



class Jejudo(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self._scope = Scope()
        self.retain = Flags.RETAIN
        self.last_result = None
        self.start_time: datetime = datetime.utcnow().replace(tzinfo=timezone.utc)
        

    @property
    def scope(self):
        """
        Gets a scope for use in REPL.
        If retention is on, this is the internal stored scope,
        otherwise it is always a new Scope.
        """

        if self.retain:
            return self._scope
        return Scope()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.reply(f"❌ ` {ctx.command.name} ` is an owner-only command. !!")


    async def jsk_python_result_handling(self, ctx: commands.Context, result):  # pylint: disable=too-many-return-statements
        """
        Determines what is done with a result when it comes out of jsk py.
        This allows you to override how this is done without having to rewrite the command itself.
        What you return is what gets stored in the temporary _ variable.
        """

        if isinstance(result, discord.Message):
            return await ctx.send(f"<Message <{result.jump_url}>>")

        if isinstance(result, discord.File):
            return await ctx.send(file=result)

        if isinstance(result, discord.Embed):
            return await ctx.send(embed=result)

        if isinstance(result, PaginatorInterface):
            return await result.send_to(ctx)

        if not isinstance(result, str):
            # repr all non-strings
            result = repr(result)

        # Eventually the below handling should probably be put somewhere else
        if len(result) <= 2000:
            if result.strip() == "":
                result = "\u200b"

            return await ctx.send(result.replace(self.bot.http.token, "[token omitted]"))

        if use_file_check(ctx, len(result)):  # File "full content" preview limit
            # Discord's desktop and web client now supports an interactive file content
            #  display for files encoded in UTF-8.
            # Since this avoids escape issues and is more intuitive than pagination for
            #  long results, it will now be prioritized over PaginatorInterface if the
            #  resultant content is below the filesize threshold
            return await ctx.send(file=discord.File(filename="output.py", fp=io.BytesIO(result.encode("utf-8"))))

        # inconsistency here, results get wrapped in codeblocks when they are too large
        #  but don't if they're not. probably not that bad, but noting for later review
        paginator = WrappedPaginator(prefix="```py", suffix="```", max_size=1985)

        paginator.add_line(result)

        interface = PaginatorInterface(ctx.bot, paginator, owner=ctx.author)
        return await interface.send_to(ctx)









# jejudo

    @commands.group("jejudo",aliases=["jeju","jds","ju"],invoke_without_command=True)
    @commands.is_owner()
    async def jejudo_jsk(self, ctx: ContextA):
        """
        The jejudo debug and diagnostic commands.
        This command on its own gives a status brief.
        All other functionality is within its subcommands.
        """
        try:

            jejudo = [
                f"> the, jejudo ` v{pkg_resources.get_distribution('jejudo').version} `, py-cord ` v{pkg_resources.get_distribution('py-cord').version} `".replace("\n", ""),
                f"ㄴ • Python ` {sys.version}`".replace("\n", ""),
                f"ㄴ • platform `{sys.platform}` • start loaded <t:{self.start_time.timestamp():.0f}:R>".replace("\n", "")
            ]
            
            if psutil:
                try:
                    proc = psutil.Process()

                    with proc.oneshot():
                        try:
                            mem = proc.memory_full_info()
                            jejudo.append(f"\n • {natural_size(mem.rss)} memory , {natural_size(mem.vms)} memory , {natural_size(mem.uss)} memory")
                        except psutil.AccessDenied:
                            pass

                        try:
                            name = proc.name()
                            pid = proc.pid
                            thread_count = proc.num_threads()

                            jejudo.append(f"ㄴ • PID {pid} (`{name}`) == {thread_count} thread(s)")
                        except psutil.AccessDenied:
                            pass

                        jejudo.append("")  # blank line
                except psutil.AccessDenied:
                    jejudo.append(
                        "ㄴ • psutil is installed, but this process does not have high enough access rights "
                    )
                    jejudo.append("")  # blank line

            cache_summary = f"` 🌐 {len(self.bot.guilds)} ` guild(s) ㅣ ` 🤴 {len(self.bot.users)} ` user(s)"

            # Show shard settings to summary
            if isinstance(self.bot, discord.AutoShardedClient):
                if len(self.bot.shards) > 20:
                    jejudo.append(
                        f"This bot is auto shards (` {len(self.bot.shards)} ` shards of ` {self.bot.shard_count} `)"
                        f"\n{cache_summary}."
                    )
                else:
                    shard_ids = ', '.join(str(i) for i in self.bot.shards.keys())
                    jejudo.append(
                        f"This bot is auto shards (Shards ` {shard_ids} ` of ` {self.bot.shard_count} `)"
                        f"\n{cache_summary}."
                    )
            elif self.bot.shard_count:
                jejudo.append(
                    f"This bot is manually sharded (Shard ` {self.bot.shard_id} ` of ` {self.bot.shard_count} `)"
                    f"\n{cache_summary}."
                )
            else:
                jejudo.append(f"This bot is not sharded\n{cache_summary}.")
            jejudo.append(f"\n\nAverage websocket latency: {round(self.bot.latency * 1000, 2)}ms")

            view = DropdownView(self.bot, ctx.author,self.start_time)
            await ctx.reply("\n".join(jejudo), view=view)
        except:
            logger.error(traceback.format_exc())

# jejudo shell

    @jejudo_jsk.command(name="shell", aliases=["bash", "sh", "powershell", "ps1", "ps", "cmd", "terminal"])
    @commands.is_owner()
    async def jejudo_shell(self, ctx: ContextA, *, argument: codeblock_converter=None):
        """
        Run a shell command
        """
        try:
            if not argument:
                await ctx.send("Usage: `<prefix> jejudo shell <argument>`")
                return
            if typing.TYPE_CHECKING:
                argument: Codeblock = argument  # type: ignore

            try:
                async with ReplResponseReactor(ctx.message):
                    with ShellReader(argument.content) as reader:
                        prefix = "```" + reader.highlight

                        paginator = WrappedPaginator(prefix=prefix, max_size=1975)
                        paginator.add_line(f"{reader.ps1} {argument.content}\n")

                        interface = PaginatorInterface(ctx.bot, paginator, owner=ctx.author)
                        self.bot.loop.create_task(interface.send_to(ctx))

                        async for line in reader:
                            if interface.closed:
                                return
                            await interface.add_line(line)

                    await interface.add_line(f"\n[ jeju status ] Return code {reader.close_code}")
            except:
                logger.error(traceback.format_exc())
        except asyncio.TimeoutError:
            pass

# jejudo shutdown

    @jejudo_jsk.command(name="shutdown", aliases=["logout", "out", "doun"])
    @commands.is_owner()
    async def jejudo_shutdown(self, ctx: ContextA):
        """
        Logs this bot out.
        """
        try:

            await ctx.send(f"__**[ ` jejudo ` ]** •  Shutdown now . . .__")
            await ctx.bot.close()
        except:
            logger.error(traceback.format_exc())

# jejudo rtt

    @jejudo_jsk.command(name="rtt", aliases=["ping"])
    @commands.is_owner()
    async def jejudo_rtt(self, ctx: ContextA):
        """
        Calculates Round-Trip Time to the API.
        """
        try:
            message = None

            # We'll show each of these readings as well as an average and standard deviation.
            api_readings: typing.List[float] = []
            # We'll also record websocket readings, but we'll only provide the average.
            websocket_readings: typing.List[float] = []

            # We do 6 iterations here.
            # This gives us 5 visible readings, because a request can't include the stats for itself.
            for _ in range(6):
                # First generate the text
                text = ""
                text += "\n".join(f"Reading {index + 1}: {reading * 1000:.2f}ms" for index, reading in enumerate(api_readings))

                if api_readings:
                    average, stddev = mean_stddev(api_readings)

                    text += f"\n\nAverage: {average * 1000:.2f} \N{PLUS-MINUS SIGN} {stddev * 1000:.2f}ms"
                else:
                    text += "\n\nNo readings yet."

                if websocket_readings:
                    average = sum(websocket_readings) / len(websocket_readings)

                    text += f"\nWebsocket latency: {average * 1000:.2f}ms"
                else:
                    text += f"\nWebsocket latency: {self.bot.latency * 1000:.2f}ms"

                # Now do the actual request and reading
                if message:
                    before = time.perf_counter()
                    await message.edit(content=text)
                    after = time.perf_counter()

                    api_readings.append(after - before)
                else:
                    before = time.perf_counter()
                    message = await ctx.send(content=text)
                    after = time.perf_counter()

                    api_readings.append(after - before)

                # Ignore websocket latencies that are 0 or negative because they usually mean we've got bad heartbeats
                if self.bot.latency > 0.0:
                    websocket_readings.append(self.bot.latency)
        except:
            logger.error(traceback.format_exc())

# jejudo load

    @jejudo_jsk.command(name="load", aliases=["reload"])
    @commands.is_owner()
    async def jejudo_load(self, ctx: ContextA, *extensions: ExtensionConverter):  # type: ignore
        # """
        # Loads or reloads the given extension names.
        # Reports any extensions that failed to load.
        # """
        # try:
        #     extensions: typing.Iterable[typing.List[str]] = extensions  # type: ignore

        #     paginator = commands.Paginator(prefix='', suffix='')

        #     # 'jsk reload' on its own just reloads jishaku
        #     if ctx.invoked_with == 'reload' and not extensions:
        #         extensions = [['jejudo']]

        #     for extension in itertools.chain(*extensions):
        #         method, icon = (
        #             (self.bot.reload_extension, "\N{CLOCKWISE RIGHTWARDS AND LEFTWARDS OPEN CIRCLE ARROWS}")
        #             if extension in self.bot.extensions else
        #             (self.bot.load_extension, "\N{INBOX TRAY}")
        #         )

        #         try:
        #             await discord.utils.maybe_coroutine(method, extension)
        #         except Exception as exc:  # pylint: disable=broad-except
        #             if isinstance(exc, commands.ExtensionFailed) and exc.__cause__:
        #                 cause = exc.__cause__
        #                 traceback_data = ''.join(traceback.format_exception(type(cause), cause, cause.__traceback__, 8))
        #             else:
        #                 traceback_data = ''.join(traceback.format_exception(type(exc), exc, exc.__traceback__, 2))

        #             paginator.add_line(
        #                 f"{icon}\N{WARNING SIGN} `{extension}`\n```py\n{traceback_data}\n```",
        #                 empty=True
        #             )
        #         else:
        #             paginator.add_line(f"{icon} `{extension}`", empty=True)

        #     for page in paginator.pages:
        #         await ctx.send(page)
        # except:
        #     logger.error(traceback.format_exc())

        """
        Loads or reloads the given extension names.

        Reports any extensions that failed to load.
        """
        try:
            paginator = WrappedPaginator(prefix="", suffix="")

            # 'jsk reload' on its own just reloads jishaku
            if ctx.invoked_with == "reload" and not extensions:
                extensions = [["jejudo"]]

            for extension in itertools.chain(*extensions):
                method, icon = (
                    (
                        self.bot.reload_extension,
                        "\N{CLOCKWISE RIGHTWARDS AND LEFTWARDS OPEN CIRCLE ARROWS}",
                    )
                    if extension in self.bot.extensions
                    else (self.bot.load_extension, "\N{INBOX TRAY}")
                )

                try:
                    method(extension)
                except Exception as exc:  # pylint: disable=broad-except
                    traceback_data = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__, 1))

                    paginator.add_line(
                        f"{icon}\N{WARNING SIGN} `{extension}`\n```py\n{traceback_data}\n```",
                        empty=True,
                    )
                else:
                    paginator.add_line(f"{icon} `{extension}`", empty=True)

            for page in paginator.pages:
                await ctx.send(page)
        except:
            logger.error(traceback.format_exc())

# jejudo unload

    @jejudo_jsk.command(name="unload")
    @commands.is_owner()
    async def jejudo_unload(self, ctx: commands.Context, *extensions: ExtensionConverter):
        """
        Unloads the given extension names.
        Reports any extensions that failed to unload.
        """
        try:
            paginator = WrappedPaginator(prefix="", suffix="")
            icon = "\N{OUTBOX TRAY}"

            for extension in itertools.chain(*extensions):
                try:
                    self.bot.unload_extension(extension)
                except Exception as exc:  # pylint: disable=broad-except
                    traceback_data = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__, 1))

                    paginator.add_line(
                        f"{icon}\N{WARNING SIGN} `{extension}`\n```py\n{traceback_data}\n```",
                        empty=True,
                    )
                else:
                    paginator.add_line(f"{icon} `{extension}`", empty=True)

            for page in paginator.pages:
                await ctx.send(page)
        except:
            logger.error(traceback.format_exc())

# jejudo python

    @jejudo_jsk.command(name="python", aliases=["py", "eval"])
    @commands.is_owner()
    async def jejudo_python(self, ctx: ContextA, *, argument: codeblock_converter):
        """
        Direct evaluation of Python code.
        """
        try:
            arg_dict = get_var_dict_from_ctx(ctx, Flags.SCOPE_PREFIX)
            arg_dict["_"] = self.last_result

            scope = self.scope

            try:
                async with ReplResponseReactor(ctx.message):

                    executor = AsyncCodeExecutor(argument.content, scope, arg_dict=arg_dict)
                    async for send, result in AsyncSender(executor):
                        if result is None:
                            continue

                        self.last_result = result

                        send(await self.jsk_python_result_handling(ctx, result))

            finally:
                scope.clear_intersection(arg_dict)
        except:
            logger.error(traceback.format_exc())

# tag

    @commands.group("tag", invoke_without_command=True)
    async def tag_tag(self, ctx, tag=None):
        try:
            if not tag:
                await ctx.send("Usage: `<prefix> tag <tag>`")
                return
            
            with open(f"{Directory}/data.json", "r",encoding="utf-8-sig") as json_file:
                dbb=json.load(json_file)
            if tag in dbb.keys():
                return await ctx.send(f"{dbb[str(tag)]['value']}")
            else:
                return await ctx.send(f"The tag {tag} could not be found.")
                
        except:
            logger.error(traceback.format_exc())
            
# tag add
    
    @tag_tag.command(name="add")
    @commands.is_owner()
    async def tag_add(self, ctx, tag_name, *, tag_add):
        try:
            try:
                with open(f"{Directory}/data.json", "r",encoding="utf-8-sig") as json_file:
                    dbb=json.load(json_file)
                if dbb[str(tag_name)]["tag"] == tag_name:
                    return await ctx.send(f"`❌` Sorry.. This tag is already fixed.")
            except:
                with open(f"{Directory}/data.json", "r",encoding="utf-8-sig") as json_file:
                    dbb=json.load(json_file)
                dbb[str(tag_name)] ={
                    "tag" : str(tag_name),
                    "value" : str(tag_add)
                }
                with open(f"{Directory}/data.json", "w",encoding="utf-8-sig") as json_file:
                    json.dump(dbb,json_file,ensure_ascii = False, indent=4)
                return await ctx.send(f"`✅` Successfully created tag\n> **Tag_Name** : {tag_name}\n> **Tag_Value** : {tag_add}")
        except:
            logger.error(traceback.format_exc())

# tag update

    @tag_tag.command(name="update", aliases=["uptag"])
    @commands.is_owner()
    async def tag_update(self, ctx, tag_name, *, tag_add):
        try:
            with open(f"{Directory}/data.json", "r",encoding="utf-8-sig") as json_file:
                dbb=json.load(json_file)
            if tag_name in dbb.keys():
                dbb[str(tag_name)]["value"] = str(tag_add)
                with open(f"{Directory}/data.json", "w",encoding="utf-8-sig") as json_file:
                    json.dump(dbb,json_file,ensure_ascii = False, indent=4)
                return await ctx.send(f"`✅` Successfully update tag\n> **Tag_Name** : {tag_name}\n> **Tag_Value** : {tag_add}")
            else:
                return await ctx.send(f"The tag {tag_name} could not be found.")
        
        except:
            logger.error(traceback.format_exc())

# tag list

    @tag_tag.command(name="list")
    # @commands.is_owner()
    async def tag_list(self, ctx):
        try:
            with open(f"{Directory}/data.json", "r",encoding="utf-8-sig") as json_file:
                dbb=json.load(json_file)
            lists = list()
            for i in dbb:
                lists.append(f'{i}')
            lists = ", ".join(lists)
            return await ctx.send(f"```\n{lists}\n```")
        except:
            logger.error(traceback.format_exc())