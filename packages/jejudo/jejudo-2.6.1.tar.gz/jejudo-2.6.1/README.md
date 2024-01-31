## This module is built on top of Jishaku.
> 1. Download jishaku
> ```bash
> pip install -U "jishaku @ git+https://github.com/Gorialis/jishaku@master"
> ```


jejudo is an extension for bot developers that enables rapid prototyping, experimentation, and debugging of features for bots.

One of jejudo's core philosophies is to be dynamic and easy-to-use. Here's the two step install:

> 1. Download jejudo on the command line using pip:
> ```bash
> pip install -U jejudo
> ```
> 2. Load the extension in your bot code before it runs:
> ```python
> bot.load_extension('jejudo')
> # or
> await bot.load_extension('jejudo')
> ```
> That's it!

You can also import the module to use the command development utilities.

## Command reference

<table>
    <tr>
        <td width="60px">
            <img align="left" width="50" src="https://github.com/Gorialis/jishaku/blob/master/.github/assets/python_logo.svg">
        </td>
        <td>
            <h4>&gt; <code>jejudo [py|python] &lt;argument&gt;</code></h4>
            The Python commands execute or evaluate Python code passed into them.
            It supports simple expressions:
            <br><br> <!-- Horrifying that I have to do this -->
            <blockquote>
                <p>&gt;  <i>jejudo py 3+4</i></p>
                <img align="left" width="50" height="50" src="https://github.com/Gorialis/jishaku/blob/master/.github/assets/beep_bot.svg">
                    <p><b>Beep Bot</b></p>
                    7
            </blockquote>
            <br>
            It also supports async expressions:
            <br><br>
            <blockquote>
                <p>&gt;  <i>jejudo py await _ctx.pins()</i></p>
                <img align="left" width="50" height="50" src="https://github.com/Gorialis/jishaku/blob/master/.github/assets/beep_bot.svg">
                    <p><b>Beep Bot</b></p>
                    [&lt;Message id=123456789012345678 ...&gt;, ...]
            </blockquote>
            <br>
            You can pass in codeblocks for longer blocks of code to execute, and you can use <code>yield</code> to return intermediate results within your processing.
            <br><br>
            The <i>inspect</i> variant of the command will return a codeblock with detailed inspection information on all objects returned.
            <br><br>
            The variables available by default in all execution contexts are:
            <br><br>
            <table>
                <tr>
                    <td><code>_ctx</code></td>
                    <td>
                        The <a href="https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.Context">Context</a> that invoked the command.
                    </td>
                </tr>
                <tr>
                    <td><code>_bot</code></td>
                    <td>
                        The running <a href="https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.Bot">Bot</a> instance.
                    </td>
                </tr>
                <tr>
                    <td><code>_author</code><br><code>_channel</code><br><code>_guild</code><br><code>_me</code><br><code>_message</code><br><code>_msg</code></td>
                    <td>
                        Shortcuts for attributes on <a href="https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.Context"><code>_ctx</code></a>.
                    </td>
                </tr>
                <tr>
                    <td><code>_find</code><br><code>_get</code></td>
                    <td>
                        Shortcuts for <a href="https://discordpy.readthedocs.io/en/latest/api.html#utility-functions"><code>discord.utils</code></a> functions.
                    </td>
                </tr>
            </table>
            <br>
            The underscore prefix on the provided variables is intended to help prevent shadowing when writing large blocks of code within the command.
            <br>
            If you decide that you don't want the prefix, you can disable it by setting the <code>jejudo_NO_UNDERSCORE</code> environment variable to <code>true</code>.
            <br><br>
            Each Python command is individually scoped. That means variables you create won't be retained in later invocations.
            <br>
        </td>
    </tr>
</table>

<table>
    <tr>
        <td width="60px">
            <img align="left" width="50" src="https://github.com/Gorialis/jishaku/blob/master/.github/assets/terminal.svg">
        </td>
        <td>
            <h4>&gt; <code>jejudo [sh|shell] &lt;argument&gt;</code></h4>
            The shell command executes commands within your system shell.
            <br><br>
            If you're on Linux and are using a custom shell, jejudo will obey the <code>SHELL</code> environment variable, otherwise, it will use <code>/bin/bash</code>.
            <br>
            On Windows, jejudo will use PowerShell if it's detected, otherwise, it will use Command Prompt.
            <br><br>
        </td>
    </tr>
</table>

<table>
    <tr>
        <td width="60px">
            <img align="left" width="50" src="https://github.com/Gorialis/jishaku/blob/master/.github/assets/extension.svg">
        </td>
        <td>
            <h4>&gt; <code>jejudo [load|reload] [extensions...]</code></h4>
            <h4>&gt; <code>jejudo unload [extensions...]</code></h4>
            These commands load, reload, or unload extensions on your bot.
            <br><br>
            You can reload jejudo itself with <code>jsk reload jejudo</code>.
            <br>
            <code>jsk reload ~</code> will reload all extensions on your bot.
            <br><br>
            You can load, reload, or unload multiple extensions at once: <code>jsk reload cogs.one cogs.two</code>
            <br><br>
            <h4>&gt; <code>jejudo shutdown</code></h4>
            This command gracefully shuts down your bot.
            <br><br>
            <h4>&gt; <code>jejudo rtt</code></h4>
            This command calculates <a href="https://en.wikipedia.org/wiki/Round-trip_delay">Round-Trip Time</a> for your bot to the API. It does this by calculating response time samples, so you can tell if your bot is being slow or not.
            <br><br>
        </td>
    </tr>
</table>
